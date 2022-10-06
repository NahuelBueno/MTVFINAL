from django.shortcuts import render
from django.http import HttpResponse
from AppPeces.models import Curso

def inicio(request):
    return render(request, "AppPeces/Inicio.html")

def curso (request):

     return render(request, "AppPeces/Cursos.html")

def estudiante(request):
    
    return render(request, "AppPeces/Estudiantes.html")


def profesor(request):
    
    return render(request, "AppPeces/Profesores.html")

def entregable(request):
    
    return render(request, "AppPeces/Entregables.html")
