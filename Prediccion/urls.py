from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Prediccion.views import prediccion
from Prediccion import views

urlpatterns = [
    path('', views.prediccion, name="prediccion"),

]