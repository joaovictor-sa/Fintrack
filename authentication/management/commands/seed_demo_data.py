from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from categories.models import Category
from transactions.models import Transaction
from goals.models import Goal
import datetime


class Command(BaseCommand):
    help = 'Reseta e popula dados do usuário demo'

    def handle(self, *args, **kwargs):
        # ── Usuário demo ──
        user, _ = User.objects.get_or_create(username='demo', defaults={
            'email': 'demo@fintrack.com',
            'first_name': 'Demo',
        })
        user.set_password('demo1234')
        user.save()

        # ── Limpa dados anteriores do demo ──
        Transaction.objects.filter(user=user).delete()
        Goal.objects.filter(user=user).delete()
        Category.objects.filter(user=user).delete()

        # ── Categorias ──
        categorias_data = [
            ('Alimentação',    'Supermercado, restaurantes e delivery'),
            ('Transporte',     'Combustível, transporte público e apps'),
            ('Moradia',        'Aluguel, condomínio e contas'),
            ('Saúde',          'Plano de saúde, farmácia e consultas'),
            ('Lazer',          'Cinema, viagens e entretenimento'),
            ('Educação',       'Cursos, livros e assinaturas'),
            ('Salário',        'Renda mensal principal'),
            ('Freelance',      'Renda extra e projetos'),
        ]
        cats = {}
        for nome, desc in categorias_data:
            cats[nome] = Category.objects.create(user=user, name=nome, description=desc)

        self.stdout.write('Categorias criadas.')

        # ── Transações dos últimos 2 meses + mês atual ──
        today = datetime.date.today()

        transacoes = []

        for delta_month in range(2, -1, -1):
            month = today.month - delta_month
            year = today.year
            if month <= 0:
                month += 12
                year -= 1

            transacoes += [
                ('Salário mensal',        5500.00, 'income', 'Salário',   datetime.date(year, month, 5)),
                ('Projeto freelance',     1200.00, 'income', 'Freelance', datetime.date(year, month, 12)),
                ('Consultoria pontual',    800.00, 'income', 'Freelance', datetime.date(year, month, 20)),
            ]

            transacoes += [
                ('Supermercado',          480.00, 'expense', 'Alimentação', datetime.date(year, month, 3)),
                ('iFood - jantar',         52.90, 'expense', 'Alimentação', datetime.date(year, month, 8)),
                ('Restaurante almoço',     38.50, 'expense', 'Alimentação', datetime.date(year, month, 14)),
                ('Padaria',                21.00, 'expense', 'Alimentação', datetime.date(year, month, 18)),
                ('Supermercado 2',        210.00, 'expense', 'Alimentação', datetime.date(year, month, 22)),
            ]

            transacoes += [
                ('Combustível',           220.00, 'expense', 'Transporte', datetime.date(year, month, 2)),
                ('Uber',                   35.00, 'expense', 'Transporte', datetime.date(year, month, 10)),
                ('Metrô - recarga',        50.00, 'expense', 'Transporte', datetime.date(year, month, 15)),
            ]

            transacoes += [
                ('Aluguel',              1500.00, 'expense', 'Moradia', datetime.date(year, month, 1)),
                ('Conta de luz',           98.00, 'expense', 'Moradia', datetime.date(year, month, 7)),
                ('Internet',               99.90, 'expense', 'Moradia', datetime.date(year, month, 9)),
                ('Água',                   45.00, 'expense', 'Moradia', datetime.date(year, month, 11)),
            ]

            transacoes += [
                ('Plano de saúde',        280.00, 'expense', 'Saúde', datetime.date(year, month, 4)),
                ('Farmácia',               67.50, 'expense', 'Saúde', datetime.date(year, month, 16)),
            ]

            transacoes += [
                ('Netflix',                45.90, 'expense', 'Lazer', datetime.date(year, month, 6)),
                ('Spotify',                21.90, 'expense', 'Lazer', datetime.date(year, month, 6)),
                ('Cinema',                 60.00, 'expense', 'Lazer', datetime.date(year, month, 19)),
            ]

            transacoes += [
                ('Curso online',          129.90, 'expense', 'Educação', datetime.date(year, month, 13)),
                ('Livro técnico',          59.90, 'expense', 'Educação', datetime.date(year, month, 21)),
            ]

        for title, amount, tipo, cat_name, date in transacoes:
            Transaction.objects.create(
                user=user,
                title=title,
                amount=amount,
                type=tipo,
                category=cats[cat_name],
                date=date,
            )

        self.stdout.write(f'{len(transacoes)} transações criadas.')

        # ── Metas do mês atual ──
        metas = [
            ('Alimentação', 800.00),
            ('Transporte',  350.00),
            ('Moradia',    1800.00),
            ('Saúde',       350.00),
            ('Lazer',       200.00),
            ('Educação',    200.00),
        ]
        for cat_name, limite in metas:
            Goal.objects.create(
                user=user,
                category=cats[cat_name],
                limit_amount=limite,
                month=today.month,
                year=today.year,
            )

        self.stdout.write(f'{len(metas)} metas criadas.')
        self.stdout.write(self.style.SUCCESS('Seed concluído com sucesso!'))
