from django.forms import ModelForm
from .models import Posteos


class CreacionPosteoForm(ModelForm):
    class Meta:
        model = Posteos
        fields = ['titulo_posteo', 'descripcion_posteo', 'redaccion_posteo',]
                  
