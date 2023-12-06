from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    usuario =models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    def __str__(self):
        return self.usuario.username
@receiver(post_save, sender= User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
@receiver(post_save, sender = User)
def guardar_usuario(sender, instance, created, **kwargs):
    instance.usuario.save()














