from django.contrib import admin
from .models import Foro

class ForoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_comentario', 'usuario',)

admin.site.register(Foro, ForoAdmin)
