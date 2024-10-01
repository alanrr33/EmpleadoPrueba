from django.contrib import admin
from .models import Empleado,Habilidades
# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'nrodoc',
        'departamento',
        'trabajo',
        'nombre_completo'
    )

    def nombre_completo(self,obj):
        return obj.nombre + ' ' + obj.apellido

    search_fields = ('nrodoc',)
    list_filter = ('trabajo','habilidades','departamento')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Habilidades)
