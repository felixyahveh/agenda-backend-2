from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    correo = models.EmailField()