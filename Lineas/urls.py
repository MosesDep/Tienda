from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Lineas.views import Lineas, Fotos
from Lineas import views

urlpatterns = [
    path('', views.Lineas, name="Lineas"),
    path('Fotos/<nombre>', views.Fotos, name="Fotos"),


]