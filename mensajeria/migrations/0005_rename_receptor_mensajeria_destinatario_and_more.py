# Generated by Django 4.2.6 on 2023-12-03 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0004_alter_mensajeria_contenido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajeria',
            old_name='receptor',
            new_name='destinatario',
        ),
        migrations.RenameField(
            model_name='mensajeria',
            old_name='contenido',
            new_name='mensaje',
        ),
        migrations.RemoveField(
            model_name='mensajeria',
            name='leido',
        ),
    ]
