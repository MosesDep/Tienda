from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.


def contacto(request):

    if request.method=='POST':

        nombre=request.POST.get("name")
        correo=request.POST.get("Email")
        contenido=request.POST.get("contenido")


        email=EmailMessage("Mensaje desde Django App ", 
        "El usuario con nombre {} con la direccion de correo de {} escribe lo siguiente:\n\n {} ".format(nombre,correo,contenido),
        "", ["moises1999vene@gmail.com"], reply_to=[correo])



        email.send()
        messages.success(request, 'Message  has been Sendd ')









    return render(request, "Contacto/contacto.html")

    
