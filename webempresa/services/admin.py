from django.contrib import admin
from .models import Service

# Register your models here.

#Con esta clase podemos ver fech y hora de creacion
#y actualizacion en el admin pero no se pueden modificar
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



#Con esto agregamos el modelo al admin
admin.site.register(Service, ServiceAdmin)


