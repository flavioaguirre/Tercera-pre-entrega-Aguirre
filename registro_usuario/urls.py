from django.urls import path
from . import views

urlpatterns = [
    path('', views.creacion_usuario, name="registro_usuario"),
    path('usuario_creado/', views.UsuarioCreado.as_view(), name="usuario_creado"),
]