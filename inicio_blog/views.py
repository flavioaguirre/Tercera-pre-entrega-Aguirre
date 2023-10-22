from django.shortcuts import render
from .models import *
from .forms import *

def blog(request):
    posteos = PosteosTarjeta.objects.all().values()
    return render(request, 'inicio_blog/index.html', {'posteos': posteos})

def posteo_completo(request, id):
    posteos= PosteosTarjeta.objects.get(id=id)
    return render(request, 'inicio_blog/posteo.html', {'posteos': posteos})

# def creacion_usuario(request):
#     return render(request, 'inicio_blog/formulario.html', {})

from inicio_blog.forms import CreacionUsuarioFormulario

def CreacionUsuarioFormulario(request):
    if request.method == "POST":
        mi_formulario = CreacionUsuarioFormulario(request.POST) # Aqui me llega la informacion del html
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            usuario = CreacionUsuarioFormulario(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["correo"], contrasenia=["contrasenia"])
            usuario.save()
        return render(request, "inicio_blog/formulario.html")
    else:
            mi_formulario = CreacionUsuarioFormulario()
    return render(request, "inicio_blog/formulario.html", {"mi_formulario": mi_formulario})