from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from .models import Foro
from .forms import ForoForm

class ListadoComentarios(ListView):
    model = Foro
    context_object_name = 'foro'
    template_name = "foro/foro_discusion.html"


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


# class EliminarComentario(DeleteView):
#     model = Foro
#     template_name = "eliminar_comentario.html"
#     success_url = reverse_lazy('eliminar_comentario')
