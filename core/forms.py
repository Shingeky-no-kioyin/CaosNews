from django import forms
from django.forms import ModelForm, fields
from .models import Noticiass

class NoticiassForm(ModelForm):
    class Meta:
        model = Noticiass
        fields = ['idNoticia', 'nombreNoticias', 'cantidadNoticias', 'colaboradores', 'correo', 'categorias']