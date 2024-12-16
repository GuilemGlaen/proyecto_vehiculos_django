from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template import TemplateDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
# Local
from .forms import RegistroForm

# Create your views here.

#View Registro
def RegistroView(request):
    try:
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Usuario registrado exitosamente!')
                return HttpResponseRedirect('/')
            else:
                # Captura los errores de validación
                messages.error(request, f"Error: {form.errors.as_text()}. Por favor, reintente")
                #messages.error(request, 'Error: Registro de usuario inválido! Reintente')
                
        form = RegistroForm()
        return render(request, 'usuario/registro.html', {'RegistroForm': form})
    except TemplateDoesNotExist as error:
        return HttpResponse(f"Plantilla no encontrada: {error}")

#View Login
def LoginView(request):
    try:
        if request.method == "POST":
            LoginForm = AuthenticationForm(request, data=request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Sesión iniciada con exito!.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Error: Credenciales inválidas! Por favor, intente nuevamente.")
        
        LoginForm = AuthenticationForm()
        return render(request, "registration/login.html", {"Login_Form": LoginForm})
    
    except TemplateDoesNotExist as error:
        return HttpResponse(f"Plantilla no encontrada: {error}")
    
#View Logout
def LogoutView(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente!")
    return HttpResponseRedirect('/')