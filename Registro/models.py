from django.db import models
import os 
# Create your models here.



class usuarios(models.Model):


    email=models.EmailField(primary_key=True)
    nombre=models.CharField(max_length=100, null=True)
    apellido=models.CharField(max_length=100, null=True)
    nacimiento=models.DateField()
    foto=models.ImageField( upload_to="usuario", null=True, blank=True)
    origen=models.CharField(max_length=100, null=True)
    sexo=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)
    creado=models.DateField(auto_now=True, null=True)

     #disabled
    


    class Meta:

        verbose_name="usuario"
        verbose_name_plural="usuarios"

        def __str__(self) :
            return self.email

            



