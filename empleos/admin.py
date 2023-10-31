from django.contrib import admin
from .models import Empleos

class EmpleosAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_publicacion_empleo', 'autor_empleo',)

admin.site.register(Empleos, EmpleosAdmin)

