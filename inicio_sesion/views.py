from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'inicio_sesion.html', {
                'form': AuthenticationForm,
                'alerta': 'Usuario o contraseña incorrectos',
            })
        else:
            login(request, user)
            return redirect('inicio_blog')
