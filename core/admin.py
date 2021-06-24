from django.contrib import admin
from .models import  Categorias,Noticiass, Periodista, Usuario
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Noticiass)
admin.site.register(Periodista)
admin.site.register(Usuario)