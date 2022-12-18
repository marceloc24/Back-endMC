from operator import index
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from seminarioApp.forms import FormInscritos
from seminarioApp.models import Inscritos, Institucion
from .serializers import InscritosSerial, InstitucionSerial
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

#Class Views Inscritos
class InscritosList(APIView):
    def get(self, request, format=None):
        ins = Inscritos.objects.all()
        serial = InscritosSerial(ins, many=True)
        return Response(serial.data)

    def post(self, request, format=None):
        serial = InscritosSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InscritosDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ins = self.get_object(pk)
        serial = InscritosSerial(ins)
        return Response(serial.data)
    
    def put(self, request, pk, format=None):
        ins = self.get_object(pk)
        serial = InscritosSerial(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        ins = self.get_object(pk)
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Function views institucion
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        ins = Institucion.objects.all()
        serial = InstitucionSerial(ins, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        ins = Institucion.objects.get(pk=id)
    except ins.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serial = InstitucionSerial(ins)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerial(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Json Institucion
def institucionDB(request):
    ins = Institucion.objects.all()
    data = {'institucion': list(ins.values('id','nombre'))}
    return JsonResponse(data)
#Json Inscripciones
def inscripcionDB(request):
    ins = Inscritos.objects.all()
    data = {'inscritos': list(ins.values('id','nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion'))}
    return JsonResponse(data)

#Crud Inscritos
def index(request):
    return render(request, 'index.html')

def listadoInscritos(request):
    inscripcion = Inscritos.objects.all
    data = {'inscripciones': inscripcion}
    return render(request, 'inscritos.html', data)

def agregarInscritos(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
            return listadoInscritos(request)
    data = {'form': form}
    return render(request, 'agregarinscritos.html', data)

def actualizarInscritos(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            return listadoInscritos(request)
    data = {'form': form}
    return render(request, 'actualizarinscritos.html', data)

def eliminarInscritos(request, id):
    reserva = Inscritos.objects.get(id = id)
    reserva.delete()
    return redirect('/lista')