from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

#CREANDO MODELO DE Categoría de Noticias
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID')
    nombreCategoria = models.CharField( max_length=50, verbose_name='Categoría')

    def __str__(self):
        return self.nombreCategoria


#CREANDO MODELO DE Noticias
class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True, verbose_name='ID')
    autor = models.CharField(max_length=50, verbose_name='Nombre de la Noticia')
    cantidad = models.IntegerField(verbose_name='Cantidad de Noticias Subidas')
    colaboradores = models.CharField(max_length=50, null=True, blank=True, verbose_name='Autor')
    correo = models.EmailField(max_length=60, verbose_name='Correo electrónico')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.autor