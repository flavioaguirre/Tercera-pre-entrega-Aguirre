from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from .models import Foro
from .forms import ForoForm


class ListadoComentarios(ListView):
    model = Foro
    context_object_name = 'foro'
    template_name = "foro/foro_discusion.html"
    
    def get_queryset(self):
        return Foro.objects.all().order_by('-fecha_comentario')

@login_required
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

