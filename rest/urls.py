from django.urls import path
from rest.views import lista_noticias
from rest.views import detalle_noticia
from .viewslogin import login


urlpatterns = [
    path('noticias/listar', lista_noticias, name='lista_noticias'),
    path('noticias/detalle/<id>', detalle_noticia, name="detalle_noticia"),
    path('login', login, name="login")
]