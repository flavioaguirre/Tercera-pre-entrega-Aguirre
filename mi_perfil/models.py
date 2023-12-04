from django.db import models
from django.contrib.auth.models import User

class DatosExtrasUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia_usuario = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
