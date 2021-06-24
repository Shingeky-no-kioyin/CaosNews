from django.urls import path
from .views import PaginalPrincipal
from .views import Categoría
from .views import Contactanos
from .views import CrearUsuario
from .views import InicioSesion
from .views import Noticias
from .views import Periodistas
from .views import usuario
from .views import listarnoticias 
from .views import agregarnoticia
from .views import editarnoticia
from .views import eliminarnoticia
<<<<<<< HEAD
from .views import perfil
from .views import perfilusuario
from .views import listarusuario
from .views import editarusuario
from .views import eliminarusuario
from .views import agregarusuario
from .views import usuarioPeriodista
=======
>>>>>>> 20f795bd7ab827e0bcd69073f2a51f11e24a5f61

urlpatterns = [
    path('',PaginalPrincipal, name="PaginalPrincipal"),
    path('Categoría/',Categoría, name="Categoría"),
    path('Contactanos/',Contactanos, name="Contactanos"),
    path('CrearUsuario/',CrearUsuario, name="CrearUsuario"),
    path('InicioSesion/',InicioSesion, name="InicioSesion"),
    path('Noticias/',Noticias, name="Noticias"),
    path('Periodistas/',Periodistas, name="Periodistas"),
    path('usuario/',usuario, name="usuario"),
    path('noticias/listar',listarnoticias, name="listarnoticias"),
    path('noticias/agregar',agregarnoticia, name="agregarnoticia"),
    path('noticias/editar/<id>', editarnoticia, name="editarnoticia"),
<<<<<<< HEAD
    path('noticias/eliminar/<id>', eliminarnoticia, name="eliminarnoticia"),
    path('periodistas/verperfil', perfil, name="perfil"),
    path('usuario/verperfil', perfilusuario, name="perfilusuario"),
    path('usuario/listar', listarusuario, name='listarusuario'),
    path('usuario/editar/<id>', editarusuario, name='editarusuario'),
    path('usuario/borrar/<id>', eliminarusuario, name='eliminarusuario'),
    path('usuario/agregar', agregarusuario, name='agregarusuario'),
    path('usuarioPeriodista', usuarioPeriodista, name='usuarioPeriodista')
=======
    path('noticias/eliminar/<id>', eliminarnoticia, name="eliminarnoticia")
>>>>>>> 20f795bd7ab827e0bcd69073f2a51f11e24a5f61
]
