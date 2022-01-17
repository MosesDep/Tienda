from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Boletos.views import Boletos
from Boletos import views

urlpatterns = [
    path('', views.Boletos, name="Boletos"),
    path('qr/', views.qr, name="qr"),
    path('error/', views.error, name="error"),
    path('comprar/', views.comprar, name="comprar"),
 




]