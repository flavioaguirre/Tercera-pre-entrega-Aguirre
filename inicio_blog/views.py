from django.shortcuts import render
from .models import *

def blog(request):
    posteos = PosteosTarjeta.objects.all().values()
    return render(request, 'inicio_blog/index.html', {'posteos': posteos})

def posteo_completo(request, id):
    posteos= PosteosTarjeta.objects.get(id=id)
    return render(request, 'inicio_blog/posteo.html', {'posteos': posteos})


