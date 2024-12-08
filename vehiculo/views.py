from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import VehiculoForm

# Create your views here.

# Vista para la pagina principal 'index.html'
class IndexView(TemplateView):
    template_name = "index.html"

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()  # guarda los datos ingresados en la base de datos
            return redirect('/')  # redirije a /admin
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

# Se define vista para la barra de navegacion
def navbarView(request):
    template_name = "navbar.html"
    return render(request, template_name)