from django.db import models
from Registro.models import usuarios
from Lineas.models import lineas


# Create your models here.


class boletos(models.Model):
    destino=models.CharField(primary_key=True, max_length=100)
    precio=models.FloatField()
    salida=models.DateField()
    llegada=models.DateField()
    created=models.DateField(auto_now=True)
    foto=models.ImageField(upload_to="boletos", null=True, blank=True)
     # condicional if para poner el carousel de iamgenes 
    #agregarle nombrea ala toabla foto 


    class Meta:

        verbose_name="boleto"
        verbose_name_plural="boletos"

        def __str__(self) :
            return self.destino

 


class tickets(models.Model):
    destino=models.CharField(primary_key=True, max_length=100)
    precio=models.FloatField()
    salida=models.DateField()
    llegada=models.DateField()
    created=models.DateField(auto_now=True)
    foto=models.ImageField(upload_to="boletos", null=True, blank=True)
    


    class Meta:

        verbose_name="boleto"
        verbose_name_plural="boletos"

        def __str__(self) :
            return self.destino





   

 

class fotos(models.Model):

    iddestino=models.ForeignKey(boletos, on_delete=models.CASCADE)
    fotos=models.ImageField(upload_to="paisajes", null=True, blank=True)


    class Meta:

        verbose_name="foto"
        verbose_name_plural="fotos"





 



class tabla(models.Model):

    campo=models.CharField(max_length=100, primary_key=True)
    iduser=models.ForeignKey(usuarios, on_delete=models.CASCADE)
    precio=models.FloatField()
    cantidad=models.PositiveIntegerField()
    producto=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    fecha=models.DateTimeField(auto_now=True, null=True)
  


    class Meta:

        verbose_name="tabla"
        verbose_name_plural="tablas"