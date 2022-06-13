# Generated by Django 4.0.4 on 2022-05-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('Rut', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Correo', models.CharField(max_length=100, verbose_name='Correo')),
                ('Telefono', models.IntegerField(verbose_name='Telefono')),
                ('Region', models.CharField(max_length=100, verbose_name='Region')),
                ('Comuna', models.CharField(max_length=100, verbose_name='Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.IntegerField(primary_key=True, serialize=False, verbose_name='idMascota')),
                ('NombreMascota', models.CharField(max_length=100, verbose_name='Nombre Mascota')),
                ('RazaMascota', models.CharField(max_length=50, verbose_name='Raza Mascota')),
                ('EdadMascota', models.IntegerField(verbose_name='Edad Mascota')),
                ('Esterilizacion', models.CharField(max_length=2, verbose_name='Esterilizacion')),
            ],
        ),
    ]
