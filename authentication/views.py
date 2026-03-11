from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.management import call_command
from .forms import RegisterForm


def demo_login(request):
    # Roda o seed sempre — reseta e popula os dados demo frescos
    try:
        call_command('seed_demo_data', verbosity=0)
    except Exception:
        pass  # Se falhar, ainda tenta autenticar com o que existe

    user = authenticate(username='demo', password='demo1234')
    if user:
        login(request, user)
        return redirect('dashboard')
    return redirect('login')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
