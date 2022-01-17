from django.contrib import admin
from Lineas.models import lineas,fotos, pictures


# Register your models here.

class lineador(admin.ModelAdmin):
    pass



 


class listapictures(admin.ModelAdmin):

    pass


admin.site.register(lineas, lineador)
admin.site.register(pictures, listapictures)


