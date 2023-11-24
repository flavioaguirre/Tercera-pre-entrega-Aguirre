from django.urls import path
from . import views

urlpatterns = [
    path('discusion/', views.ListadoComentarios.as_view(), name='foro_discusion'),
    path('comentar_foro/', views.comentar_foro, name='comentar_foro'),
    # path('eliminar_comentario/<int:id>/', views.EliminarComentario.as_view(), name='eliminar_comentario'),
]
