"""
URL configuration for proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('inicio_blog.urls')),
    path('admin/', admin.site.urls),
    path('registro_usuario/',include('registro_usuario.urls')),
    path('inicio_sesion/', include('inicio_sesion.urls')),
    path('cierre_sesion/', include('cierre_sesion.urls')),
    path('empleos/', include('empleos.urls')),
]