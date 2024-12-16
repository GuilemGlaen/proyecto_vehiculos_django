from django import forms
from .models import ModeloVehiculo as Vehiculo

# Form para ingresar datos de 'vehiculo'
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']

    # Funciones para guardar en mayúsculas todos los inputs
    def clean_marca(self):
        return self.cleaned_data['marca'].upper()
    
    def clean_modelo(self):
        return self.cleaned_data['modelo'].upper()
    
    def clean_serial_carroceria(self):
        return self.cleaned_data['serial_carroceria'].upper()
    
    def clean_serial_motor(self):
        return self.cleaned_data['serial_motor'].upper()

    def clean_categoria(self):
        return self.cleaned_data['categoria'].upper()