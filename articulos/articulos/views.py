from django.shortcuts import render, redirect
from .models import Articulo
from django.http import HttpResponse
from .forms import ArticuloForm
from django.contrib import messages
import sweetify

def articulos_list(request):
    articulos = Articulo.objects.all()
    context = {'articulos': articulos} #datos de la base de datos
    # messages.success(request, 'Hola que tal')
    # sweetify.sweetalert(request, 'Westworld is awesome', text='Really... if you have the chance - watch it!', persistent='I agree!')
    return render(request, 'articulos_list.html', context)

def articulo_detail(request, pk):
    articulos = Articulo.objects.get(pk=pk)
    context = {'articulos': articulos}
    return render(request, 'articulo_detail.html', context)

def new_articulo(request):
    if request.method == 'POST':
        #guardar el nuevo articulo
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Articulo creado con éxito')
            return redirect('/articulos')
        
    else: 
        #ir al formulario en blanco
        form = ArticuloForm
        return render(request, 'new_articulo.html', {'form': form})

def edit_articulo(request, pk):
    articulos = Articulo.objects.get(pk=pk)
    form = ArticuloForm(request.POST, instance = articulos)
    if form.is_valid():
        form.save()
        messages.success(request, 'El artículo se modificó correctamente')
        return redirect('/articulos')
    print(form.errors)
    return render(request, 'edit_articulo.html', {'articulos': articulos})

def delete_articulo(request, pk):
    articulos = Articulo.objects.get(pk=pk)
    articulos.delete()
    messages.success(request, 'El artículo se eliminó correctamente')
    return redirect('/articulos')