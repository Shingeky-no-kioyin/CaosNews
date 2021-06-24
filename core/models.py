from django.db import models

# Create your models here.

#CREANDO MODELO DE Categoría de Noticias
class Categorias(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID')
    nombreCategoria = models.CharField( max_length=50, verbose_name='Categoría')

    def __str__(self):
        return self.nombreCategoria

#CREANDO MODELO DE Periodista

class Periodista(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name="Run de Periodista")
    nombre = models.CharField(max_length=35, verbose_name='Nombre Periodista')
    def __str__(self):
        return self.nombre



#CREANDO MODELO DE Noticias
class Noticiass(models.Model):
    idNoticia = models.IntegerField(primary_key=True, verbose_name='ID Noticia')
    titulo = models.CharField(max_length=50, verbose_name='Título Noticia')
    historia = models.CharField(max_length=100, verbose_name='Historia')
    fecha = models.CharField(max_length=30, verbose_name='Fecha ')
    ubicacion = models.CharField( max_length=50, verbose_name='Ubicación')
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo