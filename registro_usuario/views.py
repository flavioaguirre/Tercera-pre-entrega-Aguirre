from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# def creacion_usuario(request):
    # if request.method == "POST":
    #     mi_formulario = UsuarioNuevo(request.POST) # Aqui me llega la informacion del html
    #     print(mi_formulario)
    #     if mi_formulario.is_valid:
    #         informacion = mi_formulario.cleaned_data
    #         usuario = UsuarioNuevo(alias=informacion["alias"], email=informacion["correo"], contrasenia=["contrasenia"])
    #         usuario.save()
    #     return render(request, "inicio_blog/")
    # else:
    #         mi_formulario = CreacionUsuarioFormulario()
    # return render(request, "inicio_blog/formulario.html", {"mi_formulario": mi_formulario})


def creacion_usuario(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
            # registro usuario
                user = User.objects.create_user(username = request.POST['username'],
                password =request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio_blog')
            except:
                return render(request, 'registro.html', {
                    'mi_formulario': UserCreationForm,
                    "alerta": 'El usuario escogido ya existe'
                })
    return render(request, 'registro.html', {
            'mi_formulario': UserCreationForm,
            "alerta": 'Las contraseñas no coinciden'
        })

