from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Noticias.views import Noticias
from Noticias import views

urlpatterns = [
    path('', views.Noticias, name="Noticias"),

]