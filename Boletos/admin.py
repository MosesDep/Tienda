from django.contrib import admin
from Boletos.models import boletos, tickets


# Register your models here.












class administradortickets(admin.ModelAdmin):

    pass


admin.site.register(tickets, administradortickets)
