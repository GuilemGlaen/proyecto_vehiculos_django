# Generated by Django 4.2.17 on 2024-12-15 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_modelovehiculo_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelovehiculo',
            options={'permissions': [('view_vehiculo', 'Puede ver la lista de vehículos'), ('add_vehiculo', 'Puede añadir nuevos vehículos')]},
        ),
    ]
