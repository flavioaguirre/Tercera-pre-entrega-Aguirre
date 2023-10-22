from django import forms

class CreacionUsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
    correo = forms.EmailField()
    contrasenia = forms.PasswordInput()