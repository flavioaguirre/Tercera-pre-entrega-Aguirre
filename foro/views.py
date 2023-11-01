from django.shortcuts import render, redirect
from .models import Foro
from .forms import ForoForm


def comentar_foro(request):
    if request.method == 'POST':
        foro_form = ForoForm(request.POST)
        if foro_form.is_valid():
            datos_nuevo_comentario = foro_form.cleaned_data

            comentario = datos_nuevo_comentario.get('comentario')
            usuario = request.user

            cometario_nuevo = Foro(comentario=comentario, usuario=usuario)
            cometario_nuevo.save()
        return redirect('foro_discusion')
    else:
        return render(request, 'foro/publicar_comentario.html', {
            'foro_form': ForoForm,})

def foro(request):
    todos_los_comentarios = Foro.objects.all().order_by('-fecha_comentario')
    return render(request, 'foro/foro_discusion.html', {'foro': todos_los_comentarios})