from operator import index
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from reservas_APP.forms import FormReservas
from reservas_APP.models import reservas

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoReservas(request):
    reserva = reservas.objects.all
    data = {'reservas': reserva}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReservas()
    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'agregarreservas.html', data)

def actualizarReserva(request, id):
    reserva = reservas.objects.get(id = id)
    form = FormReservas(instance=reserva)
    if request.method == 'POST':
        form = FormReservas(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'actualizarreservas.html', data)

def eliminarReserva(request, id):
    reserva = reservas.objects.get(id = id)
    reserva.delete()
    return redirect('/lista')