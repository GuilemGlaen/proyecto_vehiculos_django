from django.urls import path
from .views import RegistroView, LoginView, LogoutView

urlpatterns = [
    path('registro/', RegistroView, name = "registro"),
    path('login/', LoginView, name = "login"),
    path('logout/', LogoutView, name = "logout")
]