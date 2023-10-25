from django.contrib import admin
from .models import Posteos

class PosteoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_posteo',)

admin.site.register(Posteos, PosteoAdmin)