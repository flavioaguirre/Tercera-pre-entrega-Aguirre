from django.urls import path
from . import views

urlpatterns = [
    path('inicio%blog/', views.blog, name ='inicio_blog')
]
