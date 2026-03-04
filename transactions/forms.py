from django import forms
from .models import Transaction
from django.db.models import Sum


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'type', 'category', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }
        # Widgets definem como o campo é renderizado no HTML. 
        # Sem isso o Django escolhe um padrão. Aqui date vira um date picker nativo do browser, 
        # description vira um textarea pequeno de 3 linhas, e amount aceita decimais com step=0.01
        # e bloqueia negativos com min=0.

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        amount = cleaned_data.get('amount')
        date = cleaned_data.get('date')
        type_ = cleaned_data.get('type')

        if type_ == 'expense' and category and amount and date:
            from goals.models import Goal
            try:
                goal = Goal.objects.get(
                    category=category,
                    month=date.month,
                    year=date.year
                )
                spent = Transaction.objects.filter(
                    category=category,
                    date__month=date.month,
                    date__year=date.year,
                    type='expense'
                ).aggregate(Sum('amount'))['amount__sum'] or 0

                # no update, exclui a própria transação da soma
                if self.instance.pk:
                    spent -= Transaction.objects.filter(pk=self.instance.pk).values_list('amount', flat=True)[0]

                if spent + amount > goal.limit_amount:
                    raise forms.ValidationError(
                        f'Meta estourada! Limite: R$ {goal.limit_amount} | '
                        f'Gasto atual: R$ {spent} | '
                        f'Esta transação: R$ {amount}'
                    )
            except Goal.DoesNotExist:
                pass

        return cleaned_data