from core.views import Noticias
from django.contrib import admin
from .models import  Categorias,Noticiass
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Noticiass)