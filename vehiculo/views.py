from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
# Local imports
from .forms import VehiculoForm
from .models import ModeloVehiculo

# Create your views here.

# View para la pagina principal 'index.html'
class IndexView(TemplateView):
    template_name = "index.html"

# View para la página 'add_vehiculo.html'
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST': #este condicional verifica si se ha presionado el boton 'enviar' o 'submit' y su método es 'POST'
        AddForm = VehiculoForm(request.POST) # Carga los datos del form una vez se ha presionado 'enviar' o 'submit'
        if AddForm.is_valid():
            AddForm.save()  # .save guardará los datos en la BD
            messages.success(request, 'El vehículo se ha guardado exitosamente.')
            return redirect('/')  # Redirije a la pagina principal
        else:
            messages.error(request, 'Error! No se han guardado los datos. Por favor, verifique los datos ingresados e inténtelo nuevamente.')
        
    AddForm = VehiculoForm() # Carga el form en la variable de contexto
    return render(request, 'vehiculo/add_vehiculo.html', {'AddForm': AddForm}) # Renderiza la plantilla y otorga la varibale de contexto a traves de un alias

# View para la pagina 'list_vehiculo.html'
@permission_required('vehiculo.view_vehiculo', raise_exception=True)
def list_vehiculo(request):
    CostoBajo = ModeloVehiculo.objects.filter(precio__lt=10000)
    CostoMedio = ModeloVehiculo.objects.filter(precio__gte=10000, precio__lte=30000)
    CostoAlto = ModeloVehiculo.objects.filter(precio__gt=30000)
    
    vehiculos = list(ModeloVehiculo.objects.all().values('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificado'))
    
    return render(request, 'vehiculo/list_vehiculo.html', {
        'vehiculos': vehiculos,
        'costo_bajo': CostoBajo,
        'costo_medio': CostoMedio,
        'costo_alto': CostoAlto,
    })   

# View para la barra de navegacion
def navbarView(request):
    template_name = "navbar.html"
    return render(request, template_name)