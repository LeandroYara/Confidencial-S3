
from ..models import Cita

def get_cita(id):
    cita = cita.objects.get(pk=id)
    return cita

def create_cita(nuevaCita):
    cita = Cita(idServicio=nuevaCita["idServicio"], 
    nombreProfesional=nuevaCita["nombreProfesional"], 
    nombreEstudiante=nuevaCita["nombreEstudiante"], 
    codigoEstudiante=nuevaCita["codigoEstudiante"],
    edificio=nuevaCita["edificio"],
    salon=nuevaCita["salon"],
    fecha=nuevaCita["fecha"])
    cita.save()
    return cita 