from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from mi_perfil.models import DatosExtrasUsuario
from .forms import LoginForm


def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=usuario, password=password)
            login(request, user)
            DatosExtrasUsuario.objects.get_or_create(user=request.user)
            return redirect('inicio_blog')
        return render(request, 'inicio_sesion.html', {
            'form': LoginForm,
            'alerta': 'Usuario o contraseña incorrectas. Verificá la información ingresada.',
            })
    return render(request, 'inicio_sesion.html', {'form': LoginForm,})