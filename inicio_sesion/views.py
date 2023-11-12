from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=usuario, password=password)
            login(request, user)
            return redirect('inicio_blog')
        return render(request, 'inicio_sesion.html', {
            'form': AuthenticationForm,
            'alerta': 'Usuario o contraseña incorrectas',
            })
    return render(request, 'inicio_sesion.html', {'form': AuthenticationForm,})