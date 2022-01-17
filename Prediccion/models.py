from django.db import models
from Registro.models import usuarios

# Create your models here.



class prediccion(models.Model):

    iduser=models.ForeignKey(usuarios, on_delete=models.CASCADE)
    resultado=models.FloatField()


    class Meta:

        verbose_name="prediccion"
        verbose_name_plural="predicciones"

         
