from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditarPerfil(UserChangeForm):
    username = forms.CharField(label='Alias')
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    password = None
    biografia_usuario = forms.CharField(label='Mi Biografía', required=False, widget=forms.Textarea)
    avatar = forms.ImageField(label='Mi Avatar', required=False)
    
    class Meta():
        model = User
        fields = ['username', 'avatar' , 'email', 'first_name', 'last_name', 'biografia_usuario',]