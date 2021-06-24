from django.shortcuts import render,redirect
from .models import Noticiass
from .forms import NoticiassForm

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

def perfil(request):
    return render(request, 'core/perfil.html')
    
def listarnoticias(request):

    noticias = Noticiass.objects.all()

    datos = {
        'noticias' : noticias
    }

    return render(request, 'core/listarnoticias.html',datos)

def agregarnoticia(request):
    form = NoticiassForm()

    datos = {
        'form' : form
    }

    if request.method == 'POST':
        form = NoticiassForm(request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje']= 'Noticia agregada correctamente'


    return render(request, 'core/agregarnoticia.html',datos)

def editarnoticia(request,id):
    
    noticias = Noticiass.objects.get(idNoticia=id)

    datos = {
        'form' : NoticiassForm(instance=noticias)
    }

    if request.method == 'POST':
        formulario = NoticiassForm(data=request.POST, instance=noticias)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos modificados correctamente'

    return render(request, 'core/editarnoticia.html', datos)

def eliminarnoticia(request,id):
    noticias = Noticiass.objects.get(idNoticia=id)
    noticias.delete()

    return redirect(to='listarnoticias')