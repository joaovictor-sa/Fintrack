from transactions.models import Transaction
from django.db.models import Sum, Max


class Dashboard:

    def __init__(self, user):
        self.user = user

    def get_data(self):
        transactions = Transaction.objects.filter(user=self.user)

        income = transactions.filter(type='income').aggregate(t=Sum('amount'))['t'] or 0
        expense = transactions.filter(type='expense').aggregate(t=Sum('amount'))['t'] or 0
        balance = income - expense
        total = transactions.count()
        higher_expenditure = transactions.filter(type='expense').aggregate(t=Max('amount'))['t'] or 0
        top_category = (
            transactions.filter(type='expense')
            .values('category__name')
            .annotate(total=Sum('amount'))
            .order_by('-total')
            .first()
        )

        return {
            'saldo': balance,
            'receitas': income,
            'despesas': expense,
            'maior_gasto': higher_expenditure,
            'categoria_maior_gasto': top_category['category__name'] if top_category else None,
            'quantidade_transacoes': total,
        }
