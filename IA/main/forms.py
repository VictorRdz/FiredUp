from django.forms import ModelForm, modelformset_factory
from django import forms
from .models import *

AÑOS_NACIMIENTO = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', 
    '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001')


# USUARIO FORMS --------------------------------------------------------------------------------------
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['correo_electronico', 'contrasena', 'nombre', 'quien_soy', 
            'fecha_de_nacimiento', 'años_de_experiencia', 'sexo', 'informacion_adicional']
        widgets = {
            'fecha_de_nacimiento': forms.SelectDateWidget(years=AÑOS_NACIMIENTO),
            'contrasena': forms.PasswordInput(),
        }


class EducacionUsuarioForm(ModelForm):
    class Meta:
        model = Educacion_Usuario
        exclude = ['usuario']
        fields = ['usuario', 'titulo', 'institucion', 'nivel', 'area']

EducacionUsuarioFormSet =  modelformset_factory(Educacion_Usuario, form=EducacionUsuarioForm)



class IdiomaUsuarioForm(ModelForm):
    class Meta:
        model = Idioma_Usuario
        exclude = ['usuario']
        fields = ['usuario', 'idioma']

IdiomaUsuarioFormSet = modelformset_factory(Idioma_Usuario, form=IdiomaUsuarioForm)



class CompetenciaUsuarioForm(ModelForm):
    class Meta:
        model = Competencia_Usuario
        exclude = ['usuario']
        fields = ['usuario', 'competencia']

CompetenciaUsuarioFormSet = modelformset_factory(Competencia_Usuario, form=CompetenciaUsuarioForm, extra=0)



class HabilidadUsuarioForm(ModelForm):
    class Meta:
        model = Habilidad_Usuario
        exclude = ['usuario']
        fields = ['usuario', 'habilidad']

HabilidadUsuarioFormSet = modelformset_factory(Habilidad_Usuario, form=HabilidadUsuarioForm, extra=0)

# VACANTE FORMS --------------------------------------------------------------------------------------
class VacanteForm(ModelForm):
    class Meta:
        model = Vacante
        exclude = ['remuneracion', ]
        fields = ['puesto', 'descripcion', 'tipo', 'departamento',
            'frecuencia', 'sexo', 'años_de_experiencia_minima', 'informacion_adicional']



class EducacionVacanteForm(ModelForm):
    class Meta:
        model = Educacion_Vacante
        exclude = ['vacante']
        fields = ['vacante', 'nivel', 'area']

EducacionVacanteFormSet =  modelformset_factory(Educacion_Vacante, form=EducacionVacanteForm)



class IdiomaVacanteForm(ModelForm):
    class Meta:
        model = Idioma_Vacante
        exclude = ['vacante']
        fields = ['vacante', 'idioma']

IdiomaVacanteFormSet = modelformset_factory(Idioma_Vacante, form=IdiomaVacanteForm)



class CompetenciaVacanteForm(ModelForm):
    class Meta:
        model = Competencia_Vacante
        exclude = ['vacante']
        fields = ['vacante', 'competencia']

CompetenciaVacanteFormSet = modelformset_factory(Competencia_Vacante, form=CompetenciaVacanteForm, extra=0)



class HabilidadVacanteForm(ModelForm):
    class Meta:
        model = Habilidad_Vacante
        exclude = ['vacante']
        fields = ['vacante', 'habilidad']

HabilidadVacanteFormSet = modelformset_factory(Habilidad_Vacante, form=HabilidadVacanteForm, extra=0)


class RemuneracionForm(ModelForm):
    class Meta:
        model = Remuneracion
        exclude = ['vacante']
        fields = ['vacante', 'minima', 'maxima', 'frecuencia']


class EdadForm(ModelForm):
    class Meta:
        model = Edad
        exclude = ['vacante']
        fields = ['vacante', 'minima', 'maxima']