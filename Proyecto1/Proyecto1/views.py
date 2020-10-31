from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre

        self.apellido=apellido

def saludo(request): # primera vista

    p1=Persona("Profesor Juan", "Diaz")
    
    temasDelCurso=["Plantillas", "Modelos", "Formulario", "Vistas", "Despliegue"]

    ahora=datetime.datetime.now()

    #doc_externo=open("C:/Users/DASTIA/Desktop/proyectdjango/Proyecto1/Proyecto1/index.html")

    #plt=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=get_template('index.html')

    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

    #documento=plt.render(ctx)

    return render(request, "index.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

def capituloC(request):

    fecha_actual=datetime.datetime.now()

    return render(request, "CapituloC.html", {"dameFecha":fecha_actual})

def capituloC2(request):

    fecha_actual=datetime.datetime.now()

    return render(request, "CapituloC2.html", {"dameFecha":fecha_actual})

def despedida(request):

    return HttpResponse("chao Alumnos")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora exactas %s
    </h2>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):

    #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>en el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)