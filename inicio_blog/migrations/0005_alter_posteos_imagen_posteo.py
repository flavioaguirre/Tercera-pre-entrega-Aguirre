# Generated by Django 4.2.6 on 2023-10-29 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_blog', '0004_alter_posteos_imagen_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteos',
            name='imagen_posteo',
            field=models.ImageField(upload_to='./static/assets/img/inicio_blog/'),
        ),
    ]