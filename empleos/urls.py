from django.urls import path
from . import views

urlpatterns = [
    path('lista_empleos/', views.lista_empleos, name='empleos'),
    path('lista_empleos/<int:id>', views.detalle_empleo, name='detalle_empleo'),
    path('publicar_empleos/', views.publicar_empleo, name='pubicar_empleos'),
]
