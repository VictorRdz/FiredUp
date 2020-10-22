from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sexo)
admin.site.register(Idioma)
admin.site.register(Nivel_Educativo)
admin.site.register(Area_Educativa)
admin.site.register(Tipo_Vacante)
admin.site.register(Departamento)
admin.site.register(Frecuencia_Remuneracion)

admin.site.register(Usuario)
admin.site.register(Remuneracion)
admin.site.register(Edad)

admin.site.register(Vacante)
admin.site.register(Postulacion)

admin.site.register(Habilidad_Usuario)
admin.site.register(Habilidad_Vacante)
admin.site.register(Competencia_Usuario)
admin.site.register(Competencia_Vacante)
admin.site.register(Educacion_Usuario)
admin.site.register(Educacion_Vacante)