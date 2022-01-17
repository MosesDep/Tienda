from django.db import models

# Create your models here.


class noticias(models.Model):

    titulo=models.CharField(primary_key=True, max_length=100)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    foto=models.ImageField(upload_to="noticias", null=True, blank=True)
    autor=models.CharField(max_length=100)
    content=models.TextField()

    class Meta:

        verbose_name="noticia"
        verbose_name_plural="noticias"
        ordering = ['-created']

        def __str__(self) :
            return self.titulo




class contenido(models.Model):

    idtitulo=models.ForeignKey(noticias, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=100)
    contenido=models.TextField()


    class Meta:

        verbose_name="contenido"
        verbose_name_plural="contenidos"

