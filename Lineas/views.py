from django.shortcuts import render
from Lineas.models import lineas, pictures, fotos
from django.core.paginator import Paginator, EmptyPage

# Create your views here.



def Lineas(request):

    linea=lineas.objects.all()
    p=Paginator(lineas.objects.all(), 3)
    page=request.GET.get('page')
    line=p.get_page(page)

    context={

        'linea':linea,
        'line':line
    }

 

     



    return render(request,"Lineas/Lineas.html",context)


    
def Fotos(request, nombre):


    picturess=pictures.objects.filter(idnombre=nombre)


    return render(request, "Lineas/fotos.html", {"pictures": picturess})



