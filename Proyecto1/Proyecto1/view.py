from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segundaVista (request):
    return HttpResponse("<br><br><h1>Ya entendimos esto, es muy simple :)</h1>")

def miNombreEs(self, nombre):
    data = f"Mi nombre es <h1>{nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Roman"
    apellido = "Valverde"

    nameList = ["Gabriel","Jimena","Ignacio","Patricia", "Natalia"]

    diccionario = {
            "nombre" : nombre,
            "apellido" : apellido,
            "nameList" : nameList
    }

    #miHtml = open("C:/Users/Ro/Desktop/Ejercicios/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = loader.get_template("template1.html")
    #plantilla = Template(miHtml.read())
    #miHtml.close()
    #miContext = Context(diccionario)
    #documento = plantilla.render(miContext)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)