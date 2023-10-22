from django.db import models
import datetime as dt

fecha_hora_actual = dt.datetime.now()

class PosteosTarjeta(models.Model):
    area_posteo = models.CharField(max_length=12)
    titulo_posteo = models.CharField(max_length=100)
    description_posteo = models.CharField(max_length=120)
    fecha_posteo = models.DateField(fecha_hora_actual)


class PosteoDetalle(models.Model):
    area_posteo = models.CharField(max_length=12)
    redaccion_posteo = models.TextField()
    autor_posteo = models.CharField(max_length=50)



