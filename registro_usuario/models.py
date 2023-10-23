from django.db import models

class Usuario(models.Model):
    alias = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasenia = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)
