from django.urls import path
from .views import mi_perfil, editar_perfil, CambioPassword, CambioExitoso

urlpatterns = [
    path('', mi_perfil, name='mi_perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar_password/', CambioPassword.as_view(), name='cambio_password'),
    path('cambio_exitoso/', CambioExitoso.as_view(), name='cambio_exitoso'),
]
