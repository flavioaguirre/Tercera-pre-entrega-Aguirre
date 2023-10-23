from django.urls import path
from . import views

urlpatterns = [
    path('inicio_blog/', views.blog, name ='inicio_blog'),
    path('inicio_blog/<int:id>', views.posteo_completo, name='posteo'),
]
