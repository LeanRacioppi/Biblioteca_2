from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
