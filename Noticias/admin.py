from django.contrib import admin
from Noticias.models import noticias, contenido



# Register your models here.


class post(admin.ModelAdmin):

    readonly_fields=('created', 'updated')




admin.site.register(noticias, post)


