from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Foro(models.Model):
    comentario = RichTextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario} comento en el foro: {self.comentario}'
