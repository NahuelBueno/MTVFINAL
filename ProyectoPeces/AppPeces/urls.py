from django.urls import path
from AppPeces.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", curso, name="Curso"),
    path("profesores/", profesor, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("entregables/", entregable, name="Entregables"),
    path("form1/", formulario1, name="Formulario1"),
    path("busquedaCursos/", busquedaCursos),
    path("buscar/", buscar),
    

    #CRUD de profesores
    
    path("leerprofes/", leerProfesores, name="ProfesoresLeer" ),
    path("crearprofes/", crearProfesores, name="ProfesoresCrear" ),
    path("eliminarprofes/<profeNombre>/", eliminarProfesores, name="EliminarProfesor" ),
    path("editarprofes/<profeNombre>/", editarProfesores, name="EditarProfesor" ),

    #CRUD de cursos Usando Clases

    path("curso/list/", ListaCurso.as_view(), name="CursosLeer"),
    path("curso/<int:pk>", DetalleCurso.as_view(), name="CursosDetalle"),
    path("curso/crear/", CrearCurso.as_view(), name="CursosCrear"),



]