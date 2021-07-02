from rest_framework.fields import REGEX_TYPE
from .serializers import NoticiassSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from core.models import Noticiass


from core.models import Noticiass

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])


#si request es por GET: entonces accedimos a una url, para listar los elementos
#si request es por POST: estamos enviando elementos a la vista, ej: desde un formulario
def lista_noticias(request):
    if request.method == 'GET':
        #listar las noticias
        noticias = Noticiass.objects.all()
        serializer = NoticiassSerializer(noticias, many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticiassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


