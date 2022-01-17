from django.db import models

# Create your models here.


class contacto(models.Model):

    correo=models.EmailField()
    fecha=models.DateField(auto_now=True)
    contenido=models.TextField()
    updated=models.DateField()


    class Meta:

        verbose_name="contacto"
        verbose_name_plural="contactos"

        def __str__(self) :
            return self.correo
