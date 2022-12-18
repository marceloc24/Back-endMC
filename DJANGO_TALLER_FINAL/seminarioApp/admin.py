from django.contrib import admin
from .models import Inscritos, Institucion

# Register your models here.
class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion']

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

admin.site.register(Inscritos, InscritosAdmin)
admin.site.register(Institucion, InstitucionAdmin)