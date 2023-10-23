from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm 

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html', {
        'form': AuthenticationForm
    })
