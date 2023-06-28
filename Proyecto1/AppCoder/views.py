from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *

# Create your views

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

def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre = data["nombre"], apellido = data["apellido"], email = data["email"])
            estudiante.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = formSetEstudiante()

    return render(request,"AppCoder/setEstudiantes.html", {"miFormulario" : miFormulario})

def setProfesor(request):
    if request.method == 'POST':
        miFormulario = formSetProfesor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre = data["nombre"], apellido = data["apellido"], email = data["email"], profesion = data["profesion"])
            profesor.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = formSetProfesor()

    return render(request,"AppCoder/setProfesores.html", {"miFormulario" : miFormulario})

def setCurso(request):
    if request.method == 'POST':
        miFormulario = formSetCurso(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(nombre = data["nombre"], comision = data["comision"])
            curso.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = formSetCurso()

    return render(request,"AppCoder/setCursos.html", {"miFormulario" : miFormulario})

def setEntregable(request):
    if request.method == 'POST':
        miFormulario = formSetEntregable(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            entregable = Entregable(nombre = data["nombre"], fechaDeEntrega = data["fechaDeEntrega"], entregado = data["entregado"])
            entregable.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = formSetEntregable()

    return render(request,"AppCoder/setEntregable.html", {"miFormulario" : miFormulario})






    """ METODO VIEJO
      if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST["nombre"], apellido = request.POST["apellido"],email = request.POST["email"])
        estudiante.save()
        return render(request,"AppCoder/inicio.html")
    return render(request,"AppCoder/setEstudiantes.html") """

def getEstudiantes(request):
    return render(request,"AppCoder/getEstudiantes.html")

def buscarEstudiantes(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getEstudiantes.html", {"estudiantes": estudiantes})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

def leerEstudiantes(request):
    Estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"Estudiantes": Estudiantes} )




# PARA MAS ADELANTE #

""" def editarEstudiante(request, nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre = nombre_estudiante)

    if request.method == "POST":
        miFormulario = formSetEstudiante(request.POST)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
            miFormulario = formSetEstudiante()
            Estudiantes = Estudiante.objects.all()

            return render(request,"AppCoder/setEstudiantes.html", {"miFormulario" : miFormulario, "Estudiantes": Estudiantes})
    else:
        miFormulario = formSetEstudiante()
    return render(request,"AppCoder/editarEstudiantes.html", {"miFormulario" : miFormulario})
 """


#26/06 
""" def setEstudiantes(request):
    Estudiantes = Estudiante.objects.all()
    #return render(request, "AppCoder/estudiantes.html",{"Estudiantes": Estudiantes})
    if request.method == 'POST':
        estudiante = Estudiante(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
        estudiante.save()  
        miFormulario = formSetEstudiante()  
        return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario, "Estudiantes":Estudiantes})
    else:
        miFormulario = formSetEstudiante()
    return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario, "Estudiantes":Estudiantes}) """