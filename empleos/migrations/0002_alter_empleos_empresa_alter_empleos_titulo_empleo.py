# Generated by Django 4.2.6 on 2023-11-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleos',
            name='empresa',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='empleos',
            name='titulo_empleo',
            field=models.CharField(max_length=120),
        ),
    ]
