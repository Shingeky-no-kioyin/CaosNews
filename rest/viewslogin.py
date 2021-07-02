from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Nombre de usuario o contraseña incorrecta")

    pass_correcto = check_password(password,user.password)

    if not pass_correcto:
        return Response("Nombre de usuario o contraseña incorrecta")

    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)
