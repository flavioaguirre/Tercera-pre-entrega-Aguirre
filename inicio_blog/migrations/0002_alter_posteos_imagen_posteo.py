# Generated by Django 4.2.6 on 2023-10-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos',
            name='imagen_posteo',
            field=models.ImageField(upload_to='', verbose_name='inicio_blog/static/assets/img'),
        ),
    ]
