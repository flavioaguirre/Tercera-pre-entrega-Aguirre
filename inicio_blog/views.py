from django.shortcuts import render
from .models import Posteos


def blog(request):
    posteos = Posteos.objects.all().values()
    return render(request, 'inicio_blog/index.html', {'posteos': posteos})


def posteo_completo(request, id):
    posteos = Posteos.objects.get(id=id)
    return render(request, 'inicio_blog/posteo.html', {'posteos': posteos})
