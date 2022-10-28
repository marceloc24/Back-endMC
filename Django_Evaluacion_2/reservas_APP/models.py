from email.policy import default
from random import choices
from django.db import models

# Create your models here.

class reservas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=25)
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=200)

