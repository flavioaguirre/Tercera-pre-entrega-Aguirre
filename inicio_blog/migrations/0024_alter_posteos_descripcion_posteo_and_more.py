# Generated by Django 4.2.6 on 2023-11-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_blog', '0023_alter_posteos_imagen_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos',
            name='descripcion_posteo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posteos',
            name='titulo_posteo',
            field=models.CharField(max_length=120),
        ),
    ]