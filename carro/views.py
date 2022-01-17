from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .carro import Carro
from Boletos.models import boletos, tickets

from django.shortcuts import redirect


def agregar(request,destino):

    carro=Carro(request)

    Producto=tickets.objects.get(destino=destino)


    carro.agregar(Producto)

    return redirect("Boletos")


def eliminar(request, destino):

    carro=Carro(request)

    Producto=tickets.objects.get(destino=destino)


    carro.eliminar(Producto=Producto)

    return redirect("Boletos")


def restar(request, destino):

    carro=Carro(request)

    Producto=tickets.objects.get(destino=destino)


    carro.restar(Producto)

    return redirect("Boletos")




def limpiar(request):

    carro=Carro(request)

    carro.limpiar()


 
    return redirect("Boletos")




# Create your views here.
