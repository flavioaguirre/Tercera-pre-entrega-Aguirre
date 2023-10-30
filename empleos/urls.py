from django.urls import path
from . import views

urlpatterns = [
    path('lista_empleos/', views.empleos, name='empleos'),
]
