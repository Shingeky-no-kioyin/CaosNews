from rest.views import lista_noticias
from django.urls import path




urlpatterns = [
    path('noticias/listar', lista_noticias, name='lista_noticias')

]