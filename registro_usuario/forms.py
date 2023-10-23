from django import forms
from .models import Usuario

class UsuarioNuevo(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        