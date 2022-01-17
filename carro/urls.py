from django.urls import path
from . import views
 

app_name="carro"

urlpatterns = [
    
    path("agregar/<destino>/", views.agregar, name="agregar"),
    path("eliminar/<destino>/", views.eliminar, name="eliminar"),
    path("restar/<destino>/", views.restar, name="restar"),
    path("limpiar/", views.limpiar, name="limpiar"),


    

]