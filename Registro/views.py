from django.shortcuts import redirect, render
from Registro.models import usuarios
from django.contrib import messages
from .models import usuarios
from tkinter import messagebox as MessageBox
 


# Create your views here.



def registro(request):

    users=usuarios()


    if request.method=='POST':

            
        
        email=request.POST.get("Email")
        nombre=request.POST.get("name")
        apellido=request.POST.get("last")
        nacimiento=request.POST.get("fecha")
        foto=request.POST.get("foton")
        origen=request.POST.get("origen")
        genero=request.POST.get("genero")
        password=request.POST.get("contra")


        verificar=usuarios.objects.filter(email=request.POST.get("Email"))

        if not verificar  :
            users = usuarios(email,nombre,apellido,nacimiento,foto, origen, genero, password)
            users.save()
            return redirect("login")            
             
        else:

            messages.success(request, "Error Usuario Existente ")            




        


        





    return render (request, "Registro/registro.html")



def error(request):


        return render (request, "Registro/error.html")
