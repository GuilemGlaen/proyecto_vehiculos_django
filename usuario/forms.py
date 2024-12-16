from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
# Local imports
from vehiculo.models import ModeloVehiculo as Vehiculo

# Formulario de Registro
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Introduzca correo electrónico.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Asignación de permisos
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permisos = Permission.objects.filter(content_type=content_type, codename__in=['view_vehiculo', 'add_vehiculo'])
            user.user_permissions.add(*permisos)
        return user