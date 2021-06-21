from django.shortcuts import render
from .models import Noticia

# Create your views here.
def PaginalPrincipal(request):
    return render(request, 'core/PaginalPrincipal.html')

def Categoría(request):
    return render(request, 'core/Categoría.html')

def Contactanos(request):
    return render(request, 'core/Contactanos.html')

def CrearUsuario(request):
    return render(request, 'core/CrearUsuario.html')

def InicioSesion(request):
    return render(request, 'core/InicioSesion.html')

def Noticias(request):
    return render(request, 'core/Noticias.html')

def Periodistas(request):
    return render(request, 'core/Periodistas.html')

def usuario(request):
    return render(request, 'core/usuario.html')
    
def listarnoticias(request):

    noticias = Noticia.objects.all()

    datos = {
        'noticias' : noticias
    }

    return render(request, 'core/listarnoticias.html',datos)