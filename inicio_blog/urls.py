from django.urls import path
from . import views

urlpatterns = [
    path('inicio_blog/', views.inicio_blog, name='inicio_blog'),
    path('inicio_blog/<int:id>', views.posteo_completo, name='posteo'),
    path('inicio_blog/creacion_post',
         views.creacion_posteo, name='creacion_posteo'),
    path('inicio_blog/posteo_creado.html',
         views.posteo_creado, name='posteo_creado'),
    path('inicio_blog/mis_posts', views.mis_posteos, name='mis_posteos'),
    path('inicio_blog/<int:id>/eliminar', views.eliminar_post, name='eliminar_posteo'),
    path('inicio_blog/<int:id>/actualizar', views.actualizar_post, name='actualizar_posteo'),
#     path('inicio_blog/mejor_posteo_1', views.mejor_posteo, name='mejor_posteo1'),
]
