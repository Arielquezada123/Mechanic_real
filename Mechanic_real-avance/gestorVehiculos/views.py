from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import  VehiculoRegistrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')  
def registrarVehiculo(request):
    form=VehiculoRegistrationForm()
    if request.method=='POST':
        form=VehiculoRegistrationForm(request.POST,files=request.FILES)
        if form.is_valid():
            vehiculo=form.save(commit=False)
            vehiculo.usuario=request.user
            print("El formulario es valido")
            vehiculo.save()
            return HttpResponseRedirect(reverse("vehiculos"))
    data = {'form':form}
    return render(request,'forms/form_vehiculo.html',data)

@login_required(login_url='login')  
def vehiculoData(request):
    vehiculo=Vehiculo.objects.all()
    data={'vehiculo':vehiculo}
    return render(request,'tablas/tabla_vehiculo.html',data)


@login_required(login_url='login')  
def editarVehiculo(request,id ):
    vehiculo=Vehiculo.objects.get(id = id )
    form=VehiculoRegistrationForm(instance=vehiculo, files=request.FILES)
    if (request.method=='POST'):
        form=VehiculoRegistrationForm(request.POST,instance=vehiculo)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect(reverse("vehiculos"))
    data = {'form' : form } 
    return render (request, 'forms/form_vehiculo.html',data)
@login_required(login_url='login')  
def eliminarVehiculo(request,id):
    user = request.user
    vehiculo=Vehiculo.objects.get(id = id )
    vehiculo.delete()
    return  HttpResponseRedirect(reverse("vehiculos"))
