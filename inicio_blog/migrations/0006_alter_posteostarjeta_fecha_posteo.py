# Generated by Django 4.2.6 on 2023-10-22 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_blog', '0005_alter_posteostarjeta_fecha_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteostarjeta',
            name='fecha_posteo',
            field=models.DateField(verbose_name=datetime.datetime(2023, 10, 22, 0, 29, 42, 878224)),
        ),
    ]