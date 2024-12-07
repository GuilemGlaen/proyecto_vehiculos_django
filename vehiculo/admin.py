from django.contrib import admin
from .models import ModeloVehiculo # Importo el Modelo de 'ModeloVehiculo'

# Register your models here.

#Registro de SuperUsuario creado 'admin'
admin.site.register(ModeloVehiculo) # Registro al Super Usuario creado en el sitio de admin
