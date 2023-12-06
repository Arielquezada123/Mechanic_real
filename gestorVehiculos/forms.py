from django import forms
from .models import *
from gestorVehiculos import models
from .models import Vehiculo 

class VehiculoRegistrationForm(forms.Form):

    TIPOS = [
        ('Automovil','Automovil'),('Fúrgon','Fúrgon'),('Moto','Moto'),('Camioneta','Camioneta'),('Camión','Camión')
    ]

    patente = forms.CharField()
    color = forms.CharField()
    tipo = forms.CharField(widget=forms.Select(choices=TIPOS))

    patente.widget.attrs['class']='form-control'
    color.widget.attrs['class']='form-control'
    tipo.widget.attrs['class']='form-control'

    class Meta:
        model=Vehiculo
        exclude = ['usuario']
        fields='__all__'



class VehiculoRegistrationForm(forms.ModelForm):

    TIPOS = [
        ('Automovil','Automovil'),('Fúrgon','Fúrgon'),('Moto','Moto'),('Camioneta','Camioneta'),('Camión','Camión')
    ]

    patente = forms.CharField()
    color = forms.CharField()
    tipo = forms.CharField(widget=forms.Select(choices=TIPOS))

    patente.widget.attrs['class']='form-control'
    color.widget.attrs['class']='form-control'
    tipo.widget.attrs['class']='form-control'

    class Meta:
        model=Vehiculo
        exclude = ['usuario']
        fields='__all__'