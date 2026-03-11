from django import forms
from .models import Transaction
from categories.models import Category
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
                    user=self.user,
                    category=category,
                    month=date.month,
                    year=date.year
                )
                spent = Transaction.objects.filter(
                    user=self.user,
                    category=category,
                    date__month=date.month,
                    date__year=date.year,
                    type='expense'
                ).aggregate(Sum('amount'))['amount__sum'] or 0

                # no update, exclui a própria transação da soma
                if self.instance.pk:
                    spent -= Transaction.objects.filter(
                        pk=self.instance.pk
                    ).values_list('amount', flat=True)[0]

                if spent + amount > goal.limit_amount:
                    # Aviso mas não bloqueia — transação é salva mesmo assim
                    self.add_warning(
                        f'Atenção: meta de {category.name} será ultrapassada. '
                        f'Limite: R$ {goal.limit_amount:.2f} | '
                        f'Gasto: R$ {spent:.2f} | '
                        f'Esta transação: R$ {amount:.2f}'
                    )
            except Goal.DoesNotExist:
                pass

        return cleaned_data

    def add_warning(self, message):
        """Armazena avisos sem bloquear o salvamento."""
        if not hasattr(self, 'warnings'):
            self.warnings = []
        self.warnings.append(message)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user
        self.warnings = []
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)
