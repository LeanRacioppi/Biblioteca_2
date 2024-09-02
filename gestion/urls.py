from django.urls import path
from . import views

urlpatterns = [
    path('agregar-autor/', views.agregar_autor, name='agregar_autor'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar-libro/', views.agregar_libro, name='agregar_libro'),
    path('buscar/', views.buscar_libros, name='buscar_libros'),
    path('', views.agregar_libro, name='inicio'),  # Página principal redirige a añadir libro
]
