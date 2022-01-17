from django.shortcuts import render
from Boletos.models import  tabla, tickets
import random
import qrcode
import math 
import tempfile
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from .forms import Myform
from django.core.paginator import Paginator, EmptyPage
from carro.views import limpiar








 # Create your views here.


def Boletos(request):

     

    buscar=request.GET.get("buscar")

    boleteria=tickets.objects.all()

    p=Paginator(tickets.objects.all(), 3)
    page=request.GET.get('page')
    line=p.get_page(page)



    if buscar:
        line=tickets.objects.filter(
            Q(destino__icontains=buscar)|
            Q(precio__icontains=buscar)

        ).distinct()
        
       
    


    context={

        'boleteria':boleteria,
        'line':line
    }


    return render(request, "Boletos/Boletos.html",context)



def qr(request):

 
 

    if request.method == 'POST':

        form=Myform(request.POST)


 
        if form.is_valid():

            return redirect("comprar")
        else:

            messages.success(request, " Captcha Erronea ")


    form=Myform()
 

        





    return render(request, "Boletos/qr.html", {"form": form})





def error(request):



    return render(request, "Boletos/error.html")







def comprar(request):

# CREAMOS UNA NUEVA BASE DE DATOS POR LO TANTO DEBEMOS PLASMAR LOS DATOS DEL USUARIO CON ES TABLA Y NO CON COMPRA LA VIEJA 
    import random
    x = random.randrange(0,10,2) 
    import string
    import random

    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

    if request.method == 'POST':

        email=request.POST.get("Email")
        precio=request.POST.get("precio")
        cantidad=request.POST.get("cantidad")
        destino=request.POST.get("destino")
 
        compraofi = tabla(palabra,email,precio,cantidad, destino, email)
        compraofi.save()
        messages.success(request, "Exito Compra Realizada ")
        
        
 


        




    return render(request, "Boletos/comprar.html")







