# Generated by Django 4.2.6 on 2023-11-27 21:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mi_perfil', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DatosExtrasPerfil',
            new_name='DatosExtrasUsuario',
        ),
    ]