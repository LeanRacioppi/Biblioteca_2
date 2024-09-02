
from django.shortcuts import render, redirect
from .forms import FormularioAutor, FormularioCategoria, FormularioLibro, FormularioBusqueda
from .models import Libro

def agregar_autor(request):
    if request.method == 'POST':
        formulario = FormularioAutor(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioAutor()
    return render(request, 'gestion/agregar_autor.html', {'formulario': formulario})

def agregar_categoria(request):
    if request.method == 'POST':
        formulario = FormularioCategoria(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioCategoria()
    return render(request, 'gestion/agregar_categoria.html', {'formulario': formulario})

def agregar_libro(request):
    if request.method == 'POST':
        formulario = FormularioLibro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioLibro()
    return render(request, 'gestion/agregar_libro.html', {'formulario': formulario})

def buscar_libros(request):
    if request.method == 'GET':
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            consulta = formulario.cleaned_data['consulta']
            resultados = Libro.objects.filter(titulo__icontains=consulta)
            return render(request, 'gestion/resultados_busqueda.html', {'resultados': resultados, 'consulta': consulta})
    else:
        formulario = FormularioBusqueda()
    return render(request, 'gestion/buscar.html', {'formulario': formulario})
