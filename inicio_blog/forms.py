from django import forms
from ckeditor.fields import RichTextFormField
from django.forms import ModelForm
from .models import Posteos

class CreacionPosteoForm(forms.ModelForm):
    titulo_posteo = forms.CharField(label='Titulo del posteo')
    descripcion_posteo = forms.CharField(label='Descripcion del posteo')
    imagen_posteo = forms.ImageField(label='Imagen de portada', required=True)
    class Meta:
        model = Posteos
        fields = ['categoria_posteo', 'titulo_posteo', 'descripcion_posteo',
                   'imagen_posteo', 'redaccion_posteo']

class ActualizarPosteoForm(forms.ModelForm):
    titulo_posteo = forms.CharField(label='Titulo del posteo')
    descripcion_posteo = forms.CharField(label='Descripcion del posteo')
    imagen_posteo = forms.ImageField(label='Imagen de portada', required=True)
    redaccion_posteo = RichTextFormField(label='Redaccion del posteo')
    class Meta:
        model = Posteos
        fields = ('titulo_posteo', 'descripcion_posteo', 'imagen_posteo', 'redaccion_posteo',)
        