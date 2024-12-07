from django import forms
from .models import ModeloVehiculo as Vehiculo

# Form para ingresar datos de 'vehiculo'
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']