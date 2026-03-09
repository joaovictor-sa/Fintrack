from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='Nome')
    last_name = forms.CharField(max_length=50, label='Sobrenome')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('As senhas não coincidem')
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
