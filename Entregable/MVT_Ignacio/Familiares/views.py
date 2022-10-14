from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def agregar_familiares(request, nombre, apellido, edad, fecha):
    familiar = Familiares(nombre = nombre, apellido = apellido, edad = edad)
    # familiar = Familiares.objects.create(DOB)
    DOB = datetime.strptime(fecha, '%Y-%m-%d').date()
    familiar.DOB = DOB
    familiar.save()
    return HttpResponse(
        f"""<p>Nombre: {familiar.nombre} {familiar.apellido} - agregado correctamente"""
    )
    
def listar_familiares(request):
    
    lista = Familiares.objects.all()
    
    return render(request, 'familiares.html', {'lista_familiares':lista})