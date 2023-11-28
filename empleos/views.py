from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Empleos


class ListaEmpleos(LoginRequiredMixin, ListView):
    model = Empleos
    context_object_name = 'lista_empleos'
    template_name = "empleos/lista_empleos.html"
    
    def get_queryset(self):
        return Empleos.objects.all().order_by('-fecha_publicacion_empleo')

class PublicarEmpleo(LoginRequiredMixin,CreateView):
    model = Empleos
    template_name = "empleos/publicar_empleo.html"
    fields = ['titulo_empleo', 'empresa','descripcion_empleo']
    success_url = reverse_lazy('empleo_creado')
    
class Felicidades(TemplateView):
    template_name = "empleos/empleo_creado.html"

class DetalleEmpleo(DetailView):
    model = Empleos
    template_name = "empleos/detalle_empleo.html"

class EmpleosPublicados(LoginRequiredMixin, ListView):
    model = Empleos
    context_object_name = 'empleos_publicados'
    template_name = "empleos/empleos_publicados.html"
    
    def get_queryset(self):
        return Empleos.objects.filter(empresa=self.request.user)

class ActualizarEmpleo(UpdateView):
    model = Empleos
    template_name = "empleos/actualizar_empleo.html"
    fields = ['titulo_empleo', 'empresa','descripcion_empleo']
    success_url = reverse_lazy('empleos_publicados')

class EliminarEmpleo(DeleteView):
    model = Empleos
    template_name = "empleos/eliminar_empleo.html"
    success_url = reverse_lazy('empleos_publicados')


