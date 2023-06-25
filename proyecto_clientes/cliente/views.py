from django.shortcuts import render
from cliente.models import Cliente

from cliente.models import *
# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    numero_clientes = len(clientes)
    informacion_template = {'clientes': clientes, 'numero_clientes': numero_clientes}
    return render(request, 'clientes.html', informacion_template)