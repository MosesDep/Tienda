from math import e
from django.shortcuts import redirect, render
from Registro.models import usuarios
from django.contrib import messages
from tkinter import messagebox as MessageBox


# Create your views here.


def login(request):

    users=usuarios()


    if request.method =='POST':

        

        

        try:

            detallesusuario=usuarios.objects.get(email=request.POST.get("Email"),password=request.POST.get("contrasena") )

            

            request.session['email']=detallesusuario.email

            return redirect("inicio")




        except:

            messages.success(request, 'Usuario o Contraseña Incorrectas ')





                


             


    return render(request, "Login/login.html")






def error(request):



    return redirect("registro")




def cerrar(request):


    try:

        del request.session['email']

    except:


        return render(request, "Busapp/inicio.html")



    return render(request, "Busapp/inicio.html")
       


def contrasena(request):

 

    if request.method== 'POST':

        contra1=request.POST.get("contrasena")
        contra2=request.POST.get("contrasena2")
        

      



        if contra1 == contra2:

            usuarios.objects.filter(email=request.POST.get("correo")).update(password=request.POST.get("contrasena"))
            messages.success(request, 'Cambio Exitoso')
            return redirect("login")

        else:
            messages.success(request, 'Contraseñas Diferentes ')

        


    return render(request, "Login/contrasena.html")







def recuperar(request):



    if request.method== 'POST':


        contra1=request.POST.get("contrasena")
        contra2=request.POST.get("contrasena2")

        if contra1 == contra2:
        
            try:


                usuarios.objects.filter(email=request.POST.get("correo")).update(password=request.POST.get("contrasena") )
                messages.success(request, 'Proceso Exitoso')

            except:

                messages.success(request, 'Contraseñas Distitnas ')

 



        




















 




    