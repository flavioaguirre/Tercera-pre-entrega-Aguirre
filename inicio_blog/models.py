from django.db import models

class Posteos(models.Model):
    titulo_posteo = models.CharField(max_length=100),
    redaccion_posteo = models.CharField(max_length=3000)
    fecha_posteo = models.CharField(max_length=12)
    autor_posteo = models.CharField(max_length=50)

