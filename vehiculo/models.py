from django.db import models

# Create your models here.

#Crear una aplicación vehículo, la cual contiene las siguientes características:
#Marca: Fiat, Chevrolet, Ford y Toyota.
    #20 caracteres como máximo, y por defecto Ford.
#Modelo:
    #100 caracteres como máximo.
#Serial Carrocería:
    #50 caracteres como máximo.
#Serial Motor:
    #50 caracteres como máximo.
#Categoría: Particular, transporte y carga.
    #20 caracteres como máximo, y por defecto Particular.
#Precio.
#Fecha de creación.
#Fecha de modificación.
class ModeloVehiculo(models.Model):
    """
    Clase que define el Modelo de datos para vehiculo.
    """
    # Selectores de Marca
    Marca = (
        ('FIAT', 'FIAT'),
        ('CHEVROLET', 'CHEVROLET'),
        ('FORD', 'FORD'),
        ('TOYOTA', 'TOYOTA'),
    )

    # Selectores de categoría
    Categoria = (
        ('PARTICULAR', 'PARTICULAR'),
        ('TRANSPORTE', 'TRANSPORTE'),
        ('DE CARGA', 'DE CARGA'),
    )

    # Campos
    marca = models.CharField(max_length=20, choices=Marca, default='FORD', verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    serial_carroceria = models.CharField(max_length=50, verbose_name='Serial Carroceria')
    serial_motor = models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, choices=Categoria, default='PARTICULAR', verbose_name='Categoria')
    precio = models.IntegerField(verbose_name='Precio')
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha Registro')
    fecha_modificado = models.DateTimeField(auto_now = True, verbose_name='Última modificación')
    
    def __str__(self): 
        return f'Vehiculo marca {self.marca}, modelo {self.modelo}, categoría {self.categoria}. PRECIO: {self.precio}'
