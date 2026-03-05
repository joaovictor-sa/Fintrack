from django import forms
from .models import Goal


MONTH_CHOICES = [
    (1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'),
    (4, 'Abril'), (5, 'Maio'), (6, 'Junho'),
    (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'),
    (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro'),
]


class GoalForm(forms.ModelForm):

    month = forms.ChoiceField(choices=MONTH_CHOICES, widget=forms.Select())

    class Meta:
        model = Goal
        fields = ['category', 'limit_amount', 'month', 'year', 'description']
        widgets = {
            'category': forms.Select(),
            'limit_amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'year': forms.NumberInput(attrs={'min': '2020', 'max': '2100'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
