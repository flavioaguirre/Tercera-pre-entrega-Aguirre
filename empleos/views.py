from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from .models import Empleos


class ListaEmpleos(ListView):
    model = Empleos
    context_object_name = 'lista_empleos'
    template_name = "empleos/lista_empleos.html"

class PublicarEmpleo(CreateView):
    model = Empleos
    template_name = "empleos/publicar_empleo.html"
    fields = ['titulo_empleo', 'empresa','descripcion_empleo']
    success_url = reverse_lazy('empleo_creado')
    
class Felicidades(TemplateView):
    template_name = "empleos/empleo_creado.html"

class DetalleEmpleo(DetailView):
    model = Empleos
    template_name = "empleos/detalle_empleo.html"

class ActualizarEmpleo(UpdateView):
    model = Empleos
    template_name = "empleos/actualizar_empleo.html"
    fields = ['titulo_empleo', 'empresa','descripcion_empleo']
    success_url = reverse_lazy('empleos')

