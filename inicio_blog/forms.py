from django import forms
from ckeditor.fields import RichTextFormField
from django.forms import ModelForm
from .models import Posteos

class CreacionPosteoForm(forms.ModelForm):
    class Meta:
        model = Posteos
        fields = ['categoria_posteo', 'titulo_posteo', 'descripcion_posteo',
                   'imagen_posteo', 'redaccion_posteo']

class ActualizarPosteoForm(forms.ModelForm):
    class Meta:
        model = Posteos
        fields = ('titulo_posteo', 'descripcion_posteo', 'redaccion_posteo', 'imagen_posteo')
        