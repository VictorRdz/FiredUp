from django.forms import ModelForm, formset_factory
from .models import *

class Habilidad_Vacante_Form(ModelForm):
    class Meta:
            model = Habilidad_Vacante
            exclude = ['vacante']
            fields = ['vacante', 'habilidad', 'caracter']
            prefix = 'habilidad_vacante'

Habilidad_Vacante_FormSet = formset_factory(Habilidad_Vacante_Form)



class Competencia_Vacante_Form(ModelForm):
    class Meta:
            model = Competencia_Vacante
            exclude = ['vacante']
            fields = ['vacante', 'competencia', 'caracter']
            prefix = 'competencia_vacante'

Competencia_Vacante_FormSet = formset_factory(Competencia_Vacante_Form)



class Idioma_Vacante_Form(ModelForm):
    class Meta:
            model = Idioma_Vacante
            exclude = ['vacante']
            fields = ['vacante', 'idioma', 'nivel', 'caracter']
            prefix = 'idioma_vacante'
            
Idioma_Vacante_FormSet = formset_factory(Idioma_Vacante_Form)



class Educacion_Vacante_Form(ModelForm):
    class Meta:
            model = Educacion_Vacante
            exclude = ['vacante']
            fields = ['vacante', 'nivel', 'area', 'caracter']
            prefix = 'educacion_vacante'
            
Educacion_Vacante_FormSet = formset_factory(Educacion_Vacante_Form)



class Funcion_Vacante_Form(ModelForm):
    class Meta:
            model = Funcion_Vacante
            exclude = ['vacante']
            fields = ['vacante', 'funcion']
            prefix = 'funcion_vacante'
            
Funcion_Vacante_FormSet = formset_factory(Funcion_Vacante_Form)



class Prestacion_Vacante_Form(ModelForm):
    class Meta:
            model = Prestacion_Vacante
            exclude = ['vacante']
            fields = ['vacante', 'prestacion']
            prefix = 'presetacion_vacante'
            
Prestacion_Vacante_FormSet = formset_factory(Prestacion_Vacante_Form)



class Remuneracion_Vacante_Form(ModelForm):
    class Meta:
            model = Remuneracion_Vacante
            fields = ['minimo', 'maximo', 'frecuencia']
            prefix = 'remuneracion_vacante'
            
Remuneracion_Vacante_FormSet = formset_factory(Remuneracion_Vacante_Form)