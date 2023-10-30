from django import forms
from django.forms import ModelForm
from .models import Posteos


class CreacionPosteoForm(forms.ModelForm):
    class Meta:
        model = Posteos
        fields = ['categoria_posteo', 'titulo_posteo', 'descripcion_posteo',
                  'redaccion_posteo']
