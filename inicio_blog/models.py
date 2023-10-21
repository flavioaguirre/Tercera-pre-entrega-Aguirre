from django.db import models
import datetime as dt

fecha_hora_actual = dt.datetime.now()

class Posteos(models.Model):
    titulo_posteo = models.CharField(max_length=100)
    redaccion_posteo = models.TextField()
    fecha_posteo = models.CharField(max_length=12)
    autor_posteo = models.CharField(max_length=50)

