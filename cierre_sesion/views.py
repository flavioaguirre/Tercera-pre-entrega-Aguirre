from django.shortcuts import render, redirect
from django.contrib.auth import logout


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_blog')