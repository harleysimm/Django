from django.shortcuts import render, redirect
from .models import Vehiculo
from django.http import HttpResponseRedirect
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission



def index(request):
    vehiculos= Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'index.html', context)

@permission_required('vehiculo.add_vehiculo')
def add(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar)

    else:
        form = VehiculoForm()
        context = {'form': form}
        return render(request, 'add.html', context)

@login_required
def listar(request):
    vehiculos= Vehiculo.objects.all()

    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif vehiculo.precio > 10000 and vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'

    context = {'vehiculos': vehiculos}
    return render(request, 'listar.html', context)
