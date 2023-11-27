from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaEmpleos.as_view(), name='empleos'),
    path('publicar_empleo/', views.PublicarEmpleo.as_view(), name='pubicar_empleo'),
    path('empleo_creado/', views.Felicidades.as_view(), name='empleo_creado'),
    path('empleos_publicados/', views.EmpleosPublicados.as_view(), name='empleos_publicados'),
    path('<int:pk>/', views.DetalleEmpleo.as_view(), name='detalle_empleo'),
    path('<int:pk>/actualizar_empleo/', views.ActualizarEmpleo.as_view(), name='actualizar_empleo'),
    path('<int:pk>/eliminar_empleo/', views.EliminarEmpleo.as_view(), name='eliminar_empleo'),
]
