from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cria o usuário demo'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='demo').exists():
            User.objects.create_user(
                username='demo',
                email='demo@fintrack.com',
                password='demo1234',
                first_name='Demo'
            )
            self.stdout.write(self.style.SUCCESS('Usuário demo criado!'))
        else:
            self.stdout.write('Usuário demo já existe.')
