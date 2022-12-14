from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Curso(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} -- Camada: {self.camada}"

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()


class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()


class Entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()


