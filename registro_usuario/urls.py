from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.creacion_usuario, name="registro_usuario")
]