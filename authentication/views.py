from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


def demo_login(request):
    user = authenticate(username='demo', password='demo1234')
    if user:
        login(request, user)
        return redirect('dashboard')
    return redirect('login')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
