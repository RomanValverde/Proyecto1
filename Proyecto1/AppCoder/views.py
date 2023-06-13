from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

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
