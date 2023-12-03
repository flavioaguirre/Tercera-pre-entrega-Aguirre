from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Mensajeria(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='bandeja_entrada', on_delete=models.CASCADE)
    mensaje = RichTextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
