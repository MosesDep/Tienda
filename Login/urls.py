from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Login.views import login
from Login import views

urlpatterns = [
    path('', views.login, name="login"),
    path('error/', views.error, name="error"),
    path('cerrar/', views.cerrar, name="cerrar"),
    path('contrasena/', views.contrasena, name="contrasena"),
    path('recuperar/', views.recuperar, name="recuperar"),
   

 


]