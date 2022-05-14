from django.db import models
from django.core.signing import Signer

# Create your models here.

class Evento(models.Model):
    signer = Signer('Sinasticto')
    idServicio = models.IntegerField()
    nombreProfesional = signer.sign(models.CharField(max_length=100)) 
    nombreEstudiante = signer.sign(models.CharField(max_length=100)) 
    codigoEstudiante = signer.sign(models.IntegerField())
    edificio = signer.sign(models.CharField(max_length=50)) 
    salon = signer.sign(models.CharField(max_length=50)) 
    fecha = signer.sign(models.DateTimeField())
    def __str__(self):
        return '{}'.format(self.idServicio)  