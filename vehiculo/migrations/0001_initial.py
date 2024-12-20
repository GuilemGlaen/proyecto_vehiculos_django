# Generated by Django 5.1.4 on 2024-12-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('FIAT', 'fiat'), ('CHEVROLET', 'Chevrolet'), ('FORD', 'Ford'), ('Toyota', 'Toyota')], default='FORD', max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('serial_carroceria', models.CharField(max_length=50, verbose_name='Serial Carroceria')),
                ('serial_motor', models.CharField(max_length=50, verbose_name='Serial Motor')),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default='PARTICULAR', max_length=20, verbose_name='Categoria')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha Registro')),
                ('fecha_modificado', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
        ),
    ]
