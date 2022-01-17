from django.shortcuts import render, redirect
from Registro.models import usuarios
from django.contrib import messages
from Boletos.models import  tabla
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
import pdfkit 
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, C3
from django.http import HttpResponse
from Registro.models import usuarios
from django.db.models import Q
from Lineas.models import lineas
import os 
from Bus.settings import STATIC_URL
import time
import random
import qrcode
import math 
import tempfile
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
import string
from django.core.paginator import Paginator, EmptyPage
from carro.views import limpiar
from Login.views import cerrar






# Create your views here.

def inicio(request):




    return render(request, "Busapp/inicio.html")




def perfil(request, email):

    datos=usuarios.objects.filter(email=email)
 

     

    return render(request,"Busapp/perfil.html", {"datos":datos})



 
            
 
 





def cerrando(request):


    try:

        del request.session['email']

    except:


        return render(request, "Busapp/inicio.html")



    return render(request, "Busapp/inicio.html")



 
def editar(request, email): 

  

    if request.method == 'POST':

        email=request.POST.get("Email")
        nombre=request.POST.get("name")
        apellido=request.POST.get("last")
        foto=request.POST.get("foton")
        origen=request.POST.get("origen")
        genero=request.POST.get("genero")
        password=request.POST.get("contra")

 
        

        try:

            usuarios.objects.filter(email=request.POST.get("Email")).update(nombre=request.POST.get("name"), apellido=request.POST.get("last"), origen=request.POST.get("origen"), sexo=request.POST.get("genero"), password=request.POST.get("contra") )
            messages.success(request, "Proceso Finalizado ")

 



                
        except:

            return redirect("perfil")






    return render(request,"Busapp/editar.html")



def movimientos(request, email):

    datos=tabla.objects.filter(iduser=email)

#cambiar la lalve primeria por cualquier otra cosa 
# si esta en sesion quitar registro del menu 

    return render(request,"Busapp/movimientos.html", {"datos":datos})



def PDF(request, email):


    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

    datos=tabla.objects.filter(iduser=email)

    template=get_template("busapp/reporte.html")
    context={
        "datos":datos,
        "palabra":palabra
    }
    

        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'


    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     

    return response


#para el reporte de la plantilla actual solo pongop el render de l plantilla HTML que vamos a usar. 


def panel(request):


    return render(request, "busapp/panel.html")




def Usu(request):

    buscar=request.GET.get("buscar")

    datos=usuarios.objects.all()

    if buscar:
        datos=usuarios.objects.filter(
            Q(email__icontains=buscar)|
            Q(nombre__icontains=buscar)|
            Q(apellido__icontains=buscar)|
            Q(nacimiento__icontains=buscar)|
            Q(origen__icontains=buscar)|
            Q(sexo__icontains=buscar)|
            Q(creado__icontains=buscar)

        ).distinct()

    




    return render(request,"busapp/usuarios.html", {"datos":datos})



        

    

 

def Reporte(request):

    datos=tabla.objects.all()
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

    template=get_template("busapp/reportaje.html")
    context={
        "datos":datos,
        "palabra":palabra
    }

        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     
    
    return response





def repostar(request):



    datos=usuarios.objects.all()

    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    template=get_template("busapp/usuarioss.html")

    context={ "datos":datos,
    "palabra":palabra}

        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     
    
    return response






def vista(request):

    buscar=request.GET.get("buscar")

    datos=tabla.objects.all()

    if buscar:
        datos=tabla.objects.filter(
            Q(precio__icontains=buscar)|
            Q(cantidad__icontains=buscar)|
            Q(producto__icontains=buscar)|
            Q(fecha__icontains=buscar)
           

        ).distinct()

    


 

    return render(request,"busapp/vista.html", {"datos":datos})

 


    




def grafico(request):

    buscar=request.GET.get("buscar")

    datos=lineas.objects.all()

    if buscar:
        datos=lineas.objects.filter(
            Q(nombre__icontains=buscar)|
            Q(tipo__icontains=buscar)|
            Q(inicio__icontains=buscar)|
            Q(creadopor__icontains=buscar)|
            Q(fdescripcion__icontains=buscar)
           

        ).distinct()

    



 


    return render(request, "busapp/dashboard.html" ,{"datos":datos})

 







def detalle(request, campo):


    datos=tabla.objects.filter(campo=campo)



    return render(request, "busapp/detalles.html", {"datos":datos})




 
def reportedetalle(request, campo):

    datos=tabla.objects.filter(campo=campo)
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    template=get_template("busapp/reportedetalle.html")
    context={ "datos":datos,
        "palabra":palabra}
        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')

     
    
    return response




def individual(request, campo):

    datos=tabla.objects.filter(campo=campo)


 
    return render(request, "busapp/individual.html", {"datos":datos})


 # dos botones 





def reporteindi(request, campo):


    datos=tabla.objects.filter(campo=campo)
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    template=get_template("busapp/reporteindi.html")
    context={ "datos":datos,
    "palabra":palabra}




        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     
    
    return response





def indisu(request, email):


    datos=usuarios.objects.filter(email=email)


 
    return render(request, "busapp/indisu.html", {"datos":datos})

        
    

def report(request, email):


    datos=usuarios.objects.filter(email=email)
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    template=get_template("busapp/report.html")
    context={ "datos":datos,
    "palabra":palabra}

        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     
   
    return response



def eliminar(request, email):


    try:

        eliminados=usuarios.objects.filter(email=email)
        eliminados.delete()
        cerrar()
        messages.success(request, "Se ha Eliminado el Usuario cierra Sesion por favor ")


    except:

        messages.success(request, "Se ha Eliminado el Usuario cierra Sesion por favor ")




def eliminarindi(request, email):

    try:

        eliminados=usuarios.objects.filter(email=email)
        eliminados.delete()
        return redirect("panel")


    except:

        return redirect("inicio")









def politica(request):


    return  render(request, "Politica/politica.html")


def reportlines(request):



    datos=lineas.objects.all()
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    template=get_template("busapp/lineasreportes.html")
    context={ "datos":datos,
    "palabra":palabra}

        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     
    
    return response





def eliminarlinea(request, nombre):

    try:    

        eliminados=lineas.objects.filter(nombre=nombre)
        eliminados.delete()
        messages.success("request", "Se Elimino Correctamente")
      


    except:

        return redirect("inicio")


def lineasola(request, nombre):

    datos=lineas.objects.filter(nombre=nombre)


 
    return render(request, "busapp/lineasola.html", {"datos":datos})




def reportesolo(request, nombre):

    datos=lineas.objects.filter(nombre=nombre)
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        palabra=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    template=get_template("busapp/reportlinea.html")
    context={ "datos":datos,
    "palabra":palabra}

        
        

    html=template.render(context)
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'attachment; filename=report.pdf'

    pisaStatus=pisa.CreatePDF(
        html, dest=response
    )
    if pisaStatus.err:
        return HttpResponse('We had ' + html + 'dfdff')
     
   
    return response