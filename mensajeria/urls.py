from django.urls import path
from .views import MenuPrincipalMensajeria, BandejaEntrada, EnviarMensaje, MensajesEnviados

urlpatterns = [
    path('', MenuPrincipalMensajeria.as_view(), name='menu_mensajes'),
    path('bandeja_entrada/', BandejaEntrada.as_view(), name='bandeja_entrada'),
    path('enviar_mensaje/', EnviarMensaje.as_view(), name='enviar_mensaje'),
    path('mensajes_enviados/', MensajesEnviados.as_view(), name='mensajes_enviados'),
]
