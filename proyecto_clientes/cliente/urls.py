"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.clientes, name='clientes'),
 ]
