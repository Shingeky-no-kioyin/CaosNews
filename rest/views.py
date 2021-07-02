from .serializers import NoticiassSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Noticiass


from core.models import Noticiass

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))

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



#si request es por GET: entonces accedimos a una url, para ver el detalle de una noticia
#si request es por PUT: modificamos los datos del vehiculo cuya patente se envio por la url
#si request es por DELETE: eliminamos la noticia cuyo id sea el que se envió amla url
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_noticia(request, id):
    try:
        noticia = Noticiass.objects.get(idNoticia=id)

    except Noticiass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == "GET":
        serializer= NoticiassSerializer(noticia)
        return Response(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = NoticiassSerializer(noticia, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        noticia.delete()
        return Response(status.HTTP_204_NO_CONTENT)
