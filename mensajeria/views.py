from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.models import User

from .forms import MensajeriaForm
from .models import Mensajeria


class MenuPrincipalMensajeria(TemplateView):
    template_name = "mensajeria/menu_principal.html"


class BandejaEntrada(ListView):
    template_name = "mensajeria/bandeja_entrada.html"
    model = Mensajeria
    context_object_name = 'mensaje'

    def get_queryset(self):
        user = self.request.user
        return Mensajeria.objects.filter(destinatario=user).order_by('-fecha_envio')


class EnviarMensaje(CreateView):
    model = Mensajeria
    template_name = 'mensajeria/mensaje_form.html'
    fields = ['destinatario', 'mensaje']
    success_url = reverse_lazy('bandeja_entrada')

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)


class MensajesEnviados(ListView):
    template_name = "mensajeria/mensajes_enviados.html"
    model = Mensajeria
    context_object_name = 'mensaje'

    def get_queryset(self):
        user = self.request.user
        return Mensajeria.objects.filter(emisor=user).order_by('-fecha_envio')



