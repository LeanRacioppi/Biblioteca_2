from django import forms

from .models import Autor, Categoria, Libro

class FormularioAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'biografia']

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categorias', 'fecha_publicacion']

class FormularioBusqueda(forms.Form):
    consulta = forms.CharField(max_length=100)
