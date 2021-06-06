from django.urls import path
from .views import PaginalPrincipal
from .views import Categoría
from .views import Contactanos
from .views import CrearUsuario
from .views import InicioSesion
from .views import Noticias
from .views import Periodistas
from .views import usuario

urlpatterns = [
    path(' ',PaginalPrincipal, name="PaginalPrincipal"),
    path('Categoría/',Categoría, name="Categoría"),
    path('Contactanos/',Contactanos, name="Contactanos"),
    path('CrearUsuario/',CrearUsuario, name="CrearUsuario"),
    path('InicioSesion/',InicioSesion, name="InicioSesion"),
    path('Noticias/',Noticias, name="Noticias"),
    path('Periodistas/',Periodistas, name="Periodistas"),
    path('usuario/',usuario, name="usuario")
]
