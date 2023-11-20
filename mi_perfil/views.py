from django.shortcuts import render, redirect
from .forms import EditarPerfil

def mi_perfil(request):
    formulario = EditarPerfil(instance=request.user)
    return render(request, 'mi_perfil/mi_perfil.html', {
        'mi_formulario': formulario
    })

def editar_perfil(request):
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('mi_perfil')
    formulario = EditarPerfil(instance=request.user)
    return render(request, 'mi_perfil/editar_perfil.html', {
        'mi_formulario': formulario
    })
