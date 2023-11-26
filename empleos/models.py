from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Empleos(models.Model):
    titulo_empleo = models.CharField(max_length=100)
    descripcion_empleo = RichTextField()
    empresa = models.CharField(max_length=50)
    fecha_publicacion_empleo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo_empleo}  ----  Publicado el: {self.fecha_publicacion_empleo} '
