from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Registro.views import registro
from Registro import views

urlpatterns = [
    path('', views.registro, name="registro"),
    path('error/', views.error, name="error"),


]