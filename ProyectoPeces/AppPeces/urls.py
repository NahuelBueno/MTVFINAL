from django.urls import path
from AppPeces.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", curso, name="Curso"),
    path("profesores/", profesor, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("entregables/", entregable, name="Entregables"),
]