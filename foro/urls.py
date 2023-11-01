from django.urls import path
from . import views

urlpatterns = [
    path('discusion/', views.foro, name='foro_discusion'),
    path('comentar_foro/', views.comentar_foro, name='comentar_foro'),
]
