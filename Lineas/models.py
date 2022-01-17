from django.db import models

# Create your models here.


class lineas(models.Model):

    nombre=models.CharField(primary_key=True, max_length=100)
    tipo=models.CharField(max_length=100)
    inicio=models.DateField()
    creadorpor=models.CharField(max_length=100)
    foto=models.ImageField(upload_to="transporte", null=True, blank=True)
    descripcion=models.TextField()

    class Meta:

        verbose_name="linea"
        verbose_name_plural="lineas"

        def __str__(self) :
            return self.nombre



       



class pictures(models.Model):

    linea=models.CharField(primary_key=True, max_length=100)
    idnombre=models.ForeignKey(lineas, on_delete=models.CASCADE)
    fotos=models.ImageField(upload_to="fotolinea", null=True, blank=True)
    


    class Meta:

        verbose_name="picture"
        verbose_name_plural="pictures"


class fotos(models.Model):

    linea=models.CharField(primary_key=True, max_length=100)
    idnombre=models.ForeignKey(lineas, on_delete=models.CASCADE)
    fotos=models.ImageField(upload_to="fotolinea", null=True, blank=True)
    


    class Meta:

        verbose_name="foto"
        verbose_name_plural="fotos"