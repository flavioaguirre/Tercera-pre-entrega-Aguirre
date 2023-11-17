from django.urls import path
from .views import mi_perfil, editar_perfil

urlpatterns = [
    path('', mi_perfil, name='mi_perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
]
