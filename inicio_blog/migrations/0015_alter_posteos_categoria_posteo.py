# Generated by Django 4.2.6 on 2023-10-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_blog', '0014_alter_posteos_categoria_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos',
            name='categoria_posteo',
            field=models.CharField(choices=[('Programacion', 'Programación'), ('Robotica', 'Robótica'), ('Inteligencia Artificial', 'Inteligencia Artificial')], default='Programacion', max_length=25),
        ),
    ]
