from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import formSetEstudiante

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def curso(request):
    return render(request, "AppCoder/cursos.html")

def profesor(request):
    return render(request, "AppCoder/profesores.html")

def estudiante(request):
    return render(request, "AppCoder/estudiantes.html")

def entregable(request):
    return render(request, "AppCoder/entregables.html")

# 21/06 #
def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre = data["nombre"], apellido = data["apellido"],email = data["email"])
            estudiante.save()
        return render(request,"AppCoder/inicio.html")
    else:
        return render(request,"AppCoder/setEstudiantes.html")   

    if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST["nombre"], apellido = request.POST["apellido"],email = request.POST["email"])
        estudiante.save()
        return render(request,"AppCoder/inicio.html")
    return render(request,"AppCoder/setEstudiantes.html")

