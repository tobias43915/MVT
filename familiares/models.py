from turtle import color
from django.db import models

class familiares(models.Model):
    nombre = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    altura = models.IntegerField()

class pais_origen(models.Model):
    nombre = models.ForeignKey(familiares, on_delete=models.CASCADE,null=True)
    nacionalidad = models.CharField(max_length=64)