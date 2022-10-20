from django.shortcuts import render
from django.http import HttpResponse
from AppPeces.models import Curso , Profesor
from AppPeces.forms import FormularioCurso, FormularioProfesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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



def formulario1(request):
    
    if request.method=="POST":

        formulario1 = FormularioCurso(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            cursoF = Curso(nombre=info["curso"], camada=info["camada"])

            cursoF.save

            return render (request, "AppPeces/inicio.html")

    else: 

        formulario1=FormularioCurso() 

    return render(request, "AppPeces/form1.html", {"form1": formulario1})




def busquedaCursos(request):

    return render(request, "AppPeces/busquedaCursos.html")



def buscar(request):

    if request.GET["camada"]:

        busqueda = request.GET["camada"]

        cursos = Curso.objects.filter(camada__icontains=busqueda)

        return render(request, "AppPeces/resultados.html", {"cursos": cursos, "busqueda": busqueda})

    else:

        mensaje = "No enviaste datos."


    return HttpResponse(mensaje)


def leerProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {"teachers": profesores}

    return render(request, "AppPeces/leerprofes.html", contexto)


def crearProfesores(request):
    
    if request.method=="POST":

        formulario1 = FormularioProfesor(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            ProfesorF = Profesor(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

            ProfesorF.save

            return render (request, "AppPeces/inicio.html")

    else: 

        formulario1=FormularioProfesor() 

    return render(request, "AppPeces/profeformulario.html", {"formulario1": formulario1})



def eliminarProfesores(request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"teachers": profesores}

    return render(request, "AppPeces/leerProfesores.html", contexto)




def editarProfesores(request, profeNombre):
    
    profesor = Profesor.objects.get(nombre=profeNombre)

    if request.method == "POST":

        formulario1 = FormularioProfesor(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            profesor.nombre = info["nombre"]
            profesor.apellido = info["apellido"]
            profesor.correo = info["correo"]


            profesor.save

            return render (request, "AppPeces/inicio.html")

    else: 

        formulario1=FormularioProfesor(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "correo":profesor.correo}) 

    return render(request, "AppPeces/editarprofe.html", {"formulario1": formulario1, "nombre":profeNombre})





class ListaCurso(ListView):

    model = Curso

class DetalleCurso(DetailView):

    model = Curso

class CrearCurso(CreateView):

    model = Curso
    success_url = "AppPeces/curso/list"
    fields = ["nombre", "camada"]

class ActualizarCurso(UpdateView):

    model = Curso
    success_url = "AppPeces/curso/list"
    fields = ["nombre", "camada"]

class BorrarCurso(DeleteView):
    
    model = Curso
    success_url = "AppPeces/curso/list"






