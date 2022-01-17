from django.shortcuts import render
from Noticias.models import noticias
from django.core.paginator import Paginator, EmptyPage

# Create your views here.



def Noticias(request):

    posts=noticias.objects.all()
    p=Paginator(noticias.objects.all(), 5)
    page=request.GET.get('page')
    line=p.get_page(page)



    context={

        'posts':posts,
        'line':line
    }



    return render(request, "Noticias/Noticias.html",context)




