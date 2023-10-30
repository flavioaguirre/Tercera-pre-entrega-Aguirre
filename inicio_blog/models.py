from django.db import models
from django.contrib.auth.models import User


class Posteos(models.Model):
    titulo_posteo = models.CharField(max_length=100)
    descripcion_posteo = models.CharField(max_length=120)
    # imagen_posteo = models.ImageField(
    #     upload_to='./static/assets/img/inicio_blog/')
    redaccion_posteo = models.TextField()
    autor_posteo = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_posteo = models.DateTimeField(auto_now_add=True)
    
    
    CATEGORIAS = [
        ('Programacion', 'Programación'),
        ('Robotica', 'Robótica'),
        ('Inteligencia Artificial', 'Inteligencia Artificial'),
    ]

    categoria_posteo = models.CharField(
        max_length=25,
        choices=CATEGORIAS,
        default='Programacion',
    )

    def __str__(self):
        return f'{self.titulo_posteo}  ----  Posteado por: {self.autor_posteo} '
