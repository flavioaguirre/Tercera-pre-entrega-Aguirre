from django.db import models
from django.contrib.auth.models import User

class Empleos(models.Model):
    titulo_empleo = models.CharField(max_length=100)
    descripcion_empleo = models.TextField()
    autor_empleo = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion_empleo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo_empleo}  ----  Publicado el: {self.fecha_publicacion_empleo} '
