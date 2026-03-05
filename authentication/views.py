from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def demo_login(request):
    user = authenticate(username='demo', password='demo1234')
    if user:
        login(request, user)
        return redirect('dashboard')
    return redirect('login')
