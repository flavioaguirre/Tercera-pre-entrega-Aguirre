from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditarPerfil(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    
    class Meta():
        model = User
        fields = ['email', 'first_name', 'last_name']