from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer 
from rest_framework import serializers
import json

# Create your views here.
@api_view(['GET','POST', 'PUT','DELETE'])
def user(request):
    if request.method == 'GET':
        users = Usuario.objects.all()
        serializador = UsuarioSerializer(users,many = True)
        return Response(data=serializador.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializador = UsuarioSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()

            return Response(serializador.data,status=status.HTTP_201_CREATED)

        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        try: 
            usuar = request.data['user']
            
            us = Usuario.objects.get(user = usuar)
            us.password = request.data['password']
            us.correo = request.data['correo']

            us.save()
            #Usuario.objects.update(correo = us.correo)

            js = {
                'user': us.user,
                'password': us.password,
                'correo': us.correo
            }
            return Response(data = js,status=status.HTTP_200_OK)
        except:
            return Response(data = {'message': 'Usuario no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try: 
            usuar = request.data['user']
            us = Usuario.objects.get(user=usuar)
            us.delete()
            return Response(status=status.HTTP_200_OK)
        
        except:
            return Response(data = {'message': 'Usuario no existe'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def unUsuario(request):
    try:
        us = Usuario.objects.get(user = request.data['user'])
        ser = UsuarioSerializer(us,many=False)
        return Response(data = ser.data)

    except:
        return Response(data = {'message': 'Usuario no existe'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def logIn(request):
    try:
        us = Usuario.objects.get(user = request.data['user'], password= request.data['password'])
        ser = UsuarioSerializer(us,many=False)
        return Response(data = {'status': True})

    except:
        return Response(data = {'status': False},status=status.HTTP_400_BAD_REQUEST)
 
