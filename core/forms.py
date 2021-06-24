from django import forms
from django.forms import ModelForm, fields
from .models import Noticiass, Usuario

class NoticiassForm(ModelForm):
    class Meta:
        model = Noticiass
        fields = ['idNoticia', 'titulo', 'historia', 'fecha', 'ubicacion','categorias','periodista']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombreUsu', 'correoUsu', 'contrasenna']
