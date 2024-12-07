from django.urls import path
from .views import IndexView
from .views import add_vehiculo

urlpatterns = [
    path('', IndexView.as_view(), name = "index"),
    path('add/', add_vehiculo, name='add_vehiculo'),
]