from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def creacion_usuario(request):
    if request.method == "GET":
        return render(request, 'registro.html', {
            'mi_formulario': UserCreationForm, })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registro usuario
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio_blog')
            except:
                return render(request, 'registro.html', {
                    'mi_formulario': UserCreationForm,
                    "alerta": 'El usuario escogido ya existe'
                })
        else:
            return render(request, 'registro.html', {
                'mi_formulario': UserCreationForm,
                "alerta": 'Las contraseñas no coinciden'
            })
