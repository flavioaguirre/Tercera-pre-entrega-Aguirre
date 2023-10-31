from django import forms
from django.forms import ModelForm
from .models import Empleos


class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleos
        fields = ['titulo_empleo', 'descripcion_empleo']