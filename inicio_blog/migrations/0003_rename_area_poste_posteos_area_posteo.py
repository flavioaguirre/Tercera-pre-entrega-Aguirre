# Generated by Django 4.2.6 on 2023-10-21 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_blog', '0002_posteos_area_poste_alter_posteos_fecha_posteo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posteos',
            old_name='area_poste',
            new_name='area_posteo',
        ),
    ]
