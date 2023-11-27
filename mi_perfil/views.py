from django.shortcuts import render, redirect

from .forms import EditarPerfil
from .models import DatosExtrasUsuario

def mi_perfil(request):
    datos_extra = request.user.datosextrasusuario
    formulario = EditarPerfil(instance=request.user,initial={
        'email':request.user.email,
        })
    return render(request, 'mi_perfil/mi_perfil.html', {
        'mi_formulario': formulario,
        'biografia_usuario': datos_extra.biografia_usuario,
    })

def editar_perfil(request):
    datos_extra = request.user.datosextrasusuario
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid(): 
            usuario_biografia = formulario.cleaned_data.get('biografia_usuario')
            if usuario_biografia:
                datos_extra.biografia_usuario = usuario_biografia
                datos_extra.save()
            formulario.save()
            return redirect('mi_perfil')
    formulario = EditarPerfil(instance=request.user, initial={
        'biografia_usuario': datos_extra.biografia_usuario,
    })
    return render(request, 'mi_perfil/editar_perfil.html', {
        'mi_formulario': formulario
    })
