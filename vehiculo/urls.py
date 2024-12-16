from django.urls import path
from .views import IndexView, add_vehiculo, list_vehiculo, navbarView

urlpatterns = [
    path('', IndexView.as_view(), name = "index"),
    path('add/', add_vehiculo, name='add_vehiculo'),
    path('list/', list_vehiculo, name='list_vehiculo'),
    path('navbar/', navbarView, name = "navbar"),
]