# Generated by Django 3.2.4 on 2021-06-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_despacho', models.CharField(max_length=30)),
                ('nombre_cliente', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('productos', models.CharField(max_length=60)),
                ('peso', models.CharField(max_length=30)),
                ('medidas', models.CharField(max_length=30)),
                ('fecha_ingreso', models.CharField(max_length=30)),
                ('fecha_envio', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
    ]
