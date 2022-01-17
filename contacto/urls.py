from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from contacto.views import contacto
from contacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"),

]