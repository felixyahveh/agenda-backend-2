from django.db import models
import usuarios

# Create your models here.
class Contacto (models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    telefono = models.BigIntegerField()
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    usuario = models.ForeignKey(usuarios.models.Usuario,on_delete = models.CASCADE)

