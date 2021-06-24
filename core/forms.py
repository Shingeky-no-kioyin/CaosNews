from django import forms
from django.forms import ModelForm, fields
<<<<<<< HEAD
from .models import Noticiass, Usuario
=======
from .models import Noticiass
>>>>>>> 20f795bd7ab827e0bcd69073f2a51f11e24a5f61

class NoticiassForm(ModelForm):
    class Meta:
        model = Noticiass
<<<<<<< HEAD
        fields = ['idNoticia', 'titulo', 'historia', 'fecha', 'ubicacion','categorias','periodista']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombreUsu', 'correoUsu', 'contrasenna']
=======
        fields = ['idNoticia', 'nombreNoticias', 'cantidadNoticias', 'colaboradores', 'correo', 'categorias']
>>>>>>> 20f795bd7ab827e0bcd69073f2a51f11e24a5f61
