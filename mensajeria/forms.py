from django import forms
from .models import Mensajeria


class MensajeriaForm(forms.ModelForm):
    class Meta:
        model = Mensajeria
        fields = ['destinatario', 'mensaje']