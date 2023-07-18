from django.contrib import admin
from vehiculo.models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'precio')

admin.site.register(Vehiculo, VehiculoAdmin)
