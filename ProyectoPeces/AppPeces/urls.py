from django.urls import path
from AppPeces.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicio, name="Inicio"),
    path("cursos/", curso, name="Curso"),
    path("profesores/", profesor, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("entregables/", entregable, name="Entregables"),
    path("form1/", formulario1, name="Formulario1"),
    path("busquedaCursos/", busquedaCursos),
    path("buscar/", buscar),
    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="SingUp"),
    path("logout", LogoutView.as_view(template_name="AppPeces/logout.html"), name="Logout"),
    

    #CRUD de profesores
    
    path("leerprofes/", leerProfesores, name="ProfesoresLeer" ),
    path("crearprofes/", crearProfesores, name="ProfesoresCrear" ),
    path("eliminarprofes/<profeNombre>/", eliminarProfesores, name="EliminarProfesor" ),
    path("editarprofes/<profeNombre>/", editarProfesores, name="EditarProfesor" ),

    #CRUD de cursos Usando Clases

    path("curso/list/", ListaCurso.as_view(), name="CursosLeer"),
    path("curso/<int:pk>", DetalleCurso.as_view(), name="CursosDetalle"),
    path("curso/crear/", CrearCurso.as_view(), name="CursosCrear"),
    path("curso/editar/<int:pk>", ActualizarCurso.as_view(), name="CursosEditar"),
    path("curso/borrar/<int:pk>", BorrarCurso.as_view(), name="CursosBorrar"),


]