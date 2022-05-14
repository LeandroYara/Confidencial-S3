from .logic import logicaCitas as lc
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def cita_view(request,id):
    if request.method == 'GET':
        psicologo_dto = lc.get_cita(id)
        psicologo = serializers.serialize('json',[psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

    
@csrf_exempt
def cita_view_noid(request):
    if request.method == 'POST':
        cita_dto = lc.create_cita(json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')