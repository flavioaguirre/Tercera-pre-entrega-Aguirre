from django.urls import path
from . import views

urlpatterns = [
    path('inicio_blog/', views.blog, name ='inicio_blog')
]
