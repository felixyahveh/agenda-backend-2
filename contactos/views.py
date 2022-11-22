from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Contacto
from .serializers import ContactoSerializer
from rest_framework import serializers
import json

# Create your views here.
@api_view(['GET','POST', 'PUT','DELETE'])
def contacto(request):
    if request.method == 'GET':
        users = Contacto.objects.filter(usuario=request.data['user'])
        serializador = ContactoSerializer(users,many = True)
        return Response(data=serializador.data,status=status.HTTP_200_OK)

    
    if request.method == 'POST':
        serializador = ContactoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()

            return Response(serializador.data,status=status.HTTP_201_CREATED)

        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        try: 
            ind = int(request.data['id'])

            cont = Contacto.objects.get(id = ind)

            cont.nombre = request.data['nombre']
            cont.apellido = request.data['apellido']
            cont.telefono = request.data['telefono']
            cont.correo = request.data['correo']
            cont.direccion = request.data['direccion']

            cont.save()

            dat = {
                "id": cont.id,
                "nombre": cont.nombre,
                "apellido": cont.apellido,
                "telefono": cont.telefono,
                "correo": cont.correo,
                "direccion": cont.direccion,
                "usuario": str(cont.usuario)
            }

            return Response(data=dat,status=status.HTTP_200_OK)

        except:
            return Response(data={'message':'No existe el contacto'},status=status.HTTP_400_BAD_REQUEST)
        '''
        serializador = ContactoSerializer(cont,data=dat,many=False)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data,status=status.HTTP_201_CREATED)

        return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)'''

    if request.method == 'DELETE':
        try: 
            ind = int(request.data['id'])
            us = Contacto.objects.get(id=ind)
            us.delete()
            return Response(status=status.HTTP_200_OK)
        
        except:
            return Response(data = {'message': 'Contacto no existe'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def unContacto(request):
    try:
        cont = Contacto.objects.get(id = request.data['id'],usuario = request.data['usuario'])
        ser = ContactoSerializer(cont,many=False)
        return Response(data = ser.data,status=status.HTTP_200_OK)

    except:
        return Response(data = {'message': 'Usuario no existe'},status=status.HTTP_400_BAD_REQUEST)
        