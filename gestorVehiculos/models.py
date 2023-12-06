from django.db import models
from django.contrib.auth.models import User


class Vehiculo(models.Model):
    patente = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE) 


