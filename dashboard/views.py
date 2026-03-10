from django.views.generic import TemplateView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import Transaction
from goals.models import Goal
import datetime


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        month = today.month
        year = today.year
        user = self.request.user

        transactions_mes = Transaction.objects.filter(
            user=user, date__month=month, date__year=year
        )

        receitas = transactions_mes.filter(type='income').aggregate(
            Sum('amount'))['amount__sum'] or 0

        despesas = transactions_mes.filter(type='expense').aggregate(
            Sum('amount'))['amount__sum'] or 0

        saldo = receitas - despesas

        metas = []
        for goal in Goal.objects.filter(user=user, month=month, year=year):
            gasto = Transaction.objects.filter(
                user=user,
                category=goal.category,
                date__month=month,
                date__year=year,
                type='expense'
            ).aggregate(Sum('amount'))['amount__sum'] or 0

            porcentagem = min(int((gasto / goal.limit_amount) * 100), 100) if goal.limit_amount else 0

            metas.append({
                'goal': goal,
                'gasto': gasto,
                'porcentagem': porcentagem,
                'estourada': gasto > goal.limit_amount,
            })

        ultimas = Transaction.objects.filter(
            user=user
        ).order_by('-date', '-created_at')[:5]

        context.update({
            'receitas': receitas,
            'despesas': despesas,
            'saldo': saldo,
            'metas': metas,
            'ultimas': ultimas,
            'mes_atual': today.strftime('%B/%Y'),
        })
        return context
