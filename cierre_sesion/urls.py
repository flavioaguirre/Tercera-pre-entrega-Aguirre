from django.urls import path
from . import views

urlpatterns = [
    path('', views.cerrar_sesion, name='logout')
]
