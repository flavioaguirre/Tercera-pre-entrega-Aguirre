from django.db import models
from ckeditor.fields import RichTextField

class Empleos(models.Model):
    titulo_empleo = models.CharField(max_length=120)
    empresa = models.CharField(max_length=70)
    descripcion_empleo = RichTextField()
    fecha_publicacion_empleo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo_empleo}  ----  Publicado el: {self.fecha_publicacion_empleo} '
