from django.urls import path
from . import views
from. import forms

urlpatterns = [
    path('inicio_blog/', views.blog, name ='inicio_blog'),
    path('inicio_blog/<int:id>', views.posteo_completo, name='posteo'),
    path('inicio_blog/creacion_usuario', forms.CreacionUsuarioFormulario, name='creacion_usuario')
]
