from django import forms



class FormularioCurso(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()


class FormularioProfesor(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    