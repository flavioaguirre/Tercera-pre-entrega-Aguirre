from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Posteos
from .forms import CreacionPosteoForm
from .forms import ActualizarPosteoForm


# class Buscadorblog(ListView):
#     model= Posteos
#     context_object_name = 'lista_posteos'
#     template_name = 'inicio_blog/index.html'

def inicio_blog(request):
    busqueda_especifica = request.GET.get('titulo_posteo')
    if busqueda_especifica:
        lista_posteos = Posteos.objects.filter(
            titulo_posteo__icontains=busqueda_especifica)
    else:
        lista_posteos = Posteos.objects.all().order_by('-fecha_posteo')
    return render(request, 'inicio_blog/index.html', {'lista_posteos': lista_posteos})


def creacion_posteo(request):
    if request.method == 'POST':
        posteo_form = CreacionPosteoForm(request.POST)
        if posteo_form.is_valid():
            datos_nuevo_posteo = posteo_form.cleaned_data

            titulo = datos_nuevo_posteo.get('titulo_posteo')
            descripcion = datos_nuevo_posteo.get('descripcion_posteo')
            redaccion = datos_nuevo_posteo.get('redaccion_posteo')
            categoria = datos_nuevo_posteo.get('categoria_posteo')
            autor = request.user

            posteo_nuevo = Posteos(
                titulo_posteo=titulo, descripcion_posteo=descripcion, redaccion_posteo=redaccion,
                categoria_posteo=categoria, autor_posteo=autor)
            posteo_nuevo.save()
        return redirect('posteo_creado')
    else:
        return render(request, 'inicio_blog/creacion_post.html', {
            'posteo_form': CreacionPosteoForm,
            'alerta': 'Ingresa datos válidos por favor'})


def posteo_creado(request):
    return render(request, 'inicio_blog/posteo_creado.html',)


def posteo_completo(request, id):
    posteos = get_object_or_404(Posteos, pk=id)
    return render(request, 'inicio_blog/posteo.html', {'posteos': posteos})


def mis_posteos(request):
    lista_posteos = Posteos.objects.all()
    posteos_del_usuario = Posteos.objects.filter(autor_posteo=request.user).order_by('-fecha_posteo')
    return render(request, 'inicio_blog/mis_posts.html', {'posteos_del_usuario': posteos_del_usuario,
                  'lista_posteos': lista_posteos})


def eliminar_post(request, id):
    post_a_eliminar = Posteos.objects.get(id=id)
    post_a_eliminar.delete()
    return redirect('mis_posteos')


def actualizar_post(request, id):
    posteo_a_actualizar = Posteos.objects.get(id=id)
    if request.method == 'POST':
        posteo_form = ActualizarPosteoForm(request.POST)
        if posteo_form.is_valid():
            datos_posteo_actualizado = posteo_form.cleaned_data
            
            posteo_a_actualizar.titulo_posteo = datos_posteo_actualizado.get('titulo_posteo')
            posteo_a_actualizar.descripcion_posteo = datos_posteo_actualizado.get('descripcion_posteo')
            posteo_a_actualizar.redaccion_posteo = datos_posteo_actualizado.get('redaccion_posteo')
            
            posteo_a_actualizar.save()
            return redirect('mis_posteos')
    return render(request, 'inicio_blog/actualizar_post.html', {
        'posteo_form': ActualizarPosteoForm(initial={
            'titulo_posteo':posteo_a_actualizar.titulo_posteo,
            'descripcion_posteo':posteo_a_actualizar.descripcion_posteo,
            'redaccion_posteo':posteo_a_actualizar.redaccion_posteo,})
    })