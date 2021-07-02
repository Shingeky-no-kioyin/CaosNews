from django.db import models
from rest_framework import fields, serializers
from core.models import Noticiass

class NoticiassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticiass
        fields = ['idNoticia', 'titulo', 'historia', 'fecha', 'ubicacion','categorias','periodista']


