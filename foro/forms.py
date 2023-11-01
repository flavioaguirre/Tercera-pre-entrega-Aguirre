from django import forms
from django.forms import ModelForm
from .models import Foro

class ForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['comentario']