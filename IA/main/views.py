from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from .forms import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re, math
from collections import Counter
from django.templatetags.static import static

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
# Create your views here.
def index(request):
    return render(request, 'main/home.html', {})

def crear_usuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        usuario = usuario_form.save()
        request.session['id'] = usuario.id

        return redirect('/usuario/' + str(usuario.id))

    else:
        usuario_form = UsuarioForm()
        context = {
            'usuario_form': usuario_form,
        }
        return render(request, 'main/registro/usuario.html', context)




def detalle_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.edad = relativedelta(datetime.now(), usuario.fecha_de_nacimiento).years

    context = {
        'usuario': usuario,
    }
    return render(request, 'main/detalle/usuario.html', context)



def lista_usuario(request):
    usuarios = Usuario.objects.all()
    paginator = Paginator(usuarios, 5)

    pagina = request.GET.get('pagina')
    usuario_list = paginator.get_page(pagina)

    context = {
        'usuario_list': usuario_list
    }
    return render(request, 'main/lista/usuario.html', context)


def cerrar_sesion(request):
    request.session.flush()
    return redirect('index')


def iniciar_sesion(request):
    if request.method == 'POST':
        try:
            correo_electronico = request.POST['correo-electronico']
            contraseña = request.POST['contraseña']
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)
        except(Usuario.DoesNotExist):
            return redirect('/login')
        else:
            if usuario.contrasena == contraseña:
                request.session['id'] = usuario.id
                return redirect('/usuario/' + str(usuario.id))

        return redirect('/login')

    else:
        return render(request, 'main/registro/login.html', {})
        



def modificar_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                usuario = Usuario.objects.get(id=usuario_id)
                usuario_form = UsuarioForm(request.POST, instance=usuario)
                usuario_form.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                usuario = Usuario.objects.get(id=usuario_id)
                usuario_form = UsuarioForm(instance=usuario)
                context = {
                    'usuario_form': usuario_form,
                }
                return render(request, 'main/registro/modificar/usuario/general.html', context)

    return redirect('index')


def eliminar_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)
            request.session.flush()
            usuario.delete()

    return redirect('index')


def crear_educacion_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                educacion_form = EducacionUsuarioForm(request.POST)
                educacion = educacion_form.save(commit=False)
                educacion.usuario = Usuario.objects.get(id=usuario_id)
                educacion.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                educacion_form = EducacionUsuarioForm()
                context = {
                    'educacion_form': educacion_form,
                }
                return render(request, 'main/registro/agregar/usuario/educacion.html', context)

    return redirect('index')


def modificar_educacion_usuario(request, usuario_id, educacion_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                educacion = Educacion_Usuario.objects.get(id=educacion_id)
                educacion_form = EducacionUsuarioForm(request.POST, instance=educacion)
                educacion_form.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                educacion = Educacion_Usuario.objects.get(id=educacion_id)
                educacion_form = EducacionUsuarioForm(instance=educacion)
                context = {
                    'educacion_form': educacion_form,
                    'educacion_id': educacion_id,
                }
                return render(request, 'main/registro/modificar/usuario/educacion.html', context)

    return redirect('index')


def eliminar_educacion_usuario(request, usuario_id, educacion_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            educacion = Educacion_Usuario.objects.get(id=educacion_id)
            educacion.delete()
            return redirect('/usuario/' + str(request.session['id']))

    return redirect('index')



def crear_idioma_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                idioma_form = IdiomaUsuarioForm(request.POST)
                idioma = idioma_form.save(commit=False)
                idioma.usuario = Usuario.objects.get(id=usuario_id)
                idioma.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                idioma_form = IdiomaUsuarioForm()
                context = {
                    'idioma_form': idioma_form,
                }
                return render(request, 'main/registro/agregar/usuario/idioma.html', context)

    return redirect('index')


def modificar_idioma_usuario(request, usuario_id, idioma_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                idioma = Idioma_Usuario.objects.get(id=idioma_id)
                idioma_form = IdiomaUsuarioForm(request.POST, instance=idioma)
                idioma_form.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                idioma = Idioma_Usuario.objects.get(id=idioma_id)
                idioma_form = IdiomaUsuarioForm(instance=idioma)
                context = {
                    'idioma_form': idioma_form,
                    'idioma_id': idioma_id,
                }
                return render(request, 'main/registro/modificar/usuario/idioma.html', context)

    return redirect('index')


def eliminar_idioma_usuario(request, usuario_id, idioma_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            idioma = Idioma_Usuario.objects.get(id=idioma_id)
            idioma.delete()
            return redirect('/usuario/' + str(request.session['id']))

    return redirect('index')





def crear_habilidad_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                habilidad_form = HabilidadUsuarioForm(request.POST)
                habilidad = habilidad_form.save(commit=False)
                habilidad.usuario = Usuario.objects.get(id=usuario_id)
                habilidad.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                habilidad_form = HabilidadUsuarioForm()
                context = {
                    'habilidad_form': habilidad_form,
                }
                return render(request, 'main/registro/agregar/usuario/habilidad.html', context)

    return redirect('index')


def modificar_habilidad_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                habilidad_formset = HabilidadUsuarioFormSet(request.POST)
                if habilidad_formset.is_valid():
                    for habilidad_form in habilidad_formset:
                        habilidad = habilidad_form.save(commit=False)
                        habilidad.usuario = Usuario.objects.get(id=usuario_id)
                        habilidad.save()
                        
                    return redirect('/usuario/' + str(request.session['id']))

            else:
                usuario = Usuario.objects.get(id=usuario_id)
                habilidades = usuario.habilidad_usuario_set.all()
                habilidad_formset = HabilidadUsuarioFormSet(queryset=habilidades)
                context = {
                    'habilidad_formset': habilidad_formset,
                }
                return render(request, 'main/registro/modificar/usuario/habilidad.html', context)

    return redirect('index')


def eliminar_habilidad_usuario(request, usuario_id, habilidad_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            habilidad = Habilidad_Usuario.objects.get(id=habilidad_id)
            habilidad.delete()
            return redirect('/usuario/' + str(request.session['id']))

    return redirect('index')



def crear_competencia_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                competencia_form = CompetenciaUsuarioForm(request.POST)
                competencia = competencia_form.save(commit=False)
                competencia.usuario = Usuario.objects.get(id=usuario_id)
                competencia.save()
                    
                return redirect('/usuario/' + str(request.session['id']))

            else:
                competencia_form = CompetenciaUsuarioForm()
                context = {
                    'competencia_form': competencia_form,
                }
                return render(request, 'main/registro/agregar/usuario/competencia.html', context)

    return redirect('index')


def modificar_competencia_usuario(request, usuario_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            if request.method == 'POST':
                competencia_formset = CompetenciaUsuarioFormSet(request.POST)
                if competencia_formset.is_valid():
                    for competencia_form in competencia_formset:
                        competencia = competencia_form.save(commit=False)
                        competencia.usuario = Usuario.objects.get(id=usuario_id)
                        competencia.save()
                        
                    return redirect('/usuario/' + str(request.session['id']))

            else:
                usuario = Usuario.objects.get(id=usuario_id)
                competencias = usuario.competencia_usuario_set.all()
                competencia_formset = CompetenciaUsuarioFormSet(queryset=competencias)
                context = {
                    'competencia_formset': competencia_formset,
                }
                return render(request, 'main/registro/modificar/usuario/competencia.html', context)

    return redirect('index')


def eliminar_competencia_usuario(request, usuario_id, competencia_id):
    if 'id' in request.session:
        if request.session['id'] == usuario_id:
            competencia = Competencia_Usuario.objects.get(id=competencia_id)
            competencia.delete()
            return redirect('/usuario/' + str(request.session['id']))

    return redirect('index')


def crear_vacante(request):
    if request.method == 'POST':
        vacante_form = VacanteForm(request.POST)
        remuneracion_form = RemuneracionForm(request.POST)
        edad_form = EdadForm(request.POST)
        vacante = vacante_form.save()

        remuneracion = remuneracion_form.save(commit=False)
        remuneracion.vacante = Vacante.objects.get(id=vacante.id)
        remuneracion.save()

        edad = edad_form.save(commit=False)
        edad.vacante = Vacante.objects.get(id=vacante.id)
        edad.save()

        return redirect('/vacante/' + str(vacante.id))

    else:
        vacante_form = VacanteForm()
        remuneracion_form = RemuneracionForm()
        edad_form = EdadForm()
        context = {
            'vacante_form': vacante_form,
            'remuneracion_form': remuneracion_form,
            'edad_form': edad_form,
        }
        return render(request, 'main/registro/vacante.html', context)



def detalle_vacante(request, vacante_id):
    vacante = Vacante.objects.get(id=vacante_id)

    context = {
        'vacante': vacante,
    }
    return render(request, 'main/detalle/vacante.html', context)



def crear_educacion_vacante(request, vacante_id):
    if request.method == 'POST':
        educacion_form = EducacionVacanteForm(request.POST)
        educacion = educacion_form.save(commit=False)
        educacion.vacante = Vacante.objects.get(id=vacante_id)
        educacion.save()
            
        return redirect('/vacante/' + str(vacante_id))

    else:
        educacion_form = EducacionVacanteForm()
        context = {
            'educacion_form': educacion_form,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/agregar/vacante/educacion.html', context)

    return redirect('index')


def modificar_educacion_vacante(request, vacante_id, educacion_id):
    if request.method == 'POST':
        educacion = Educacion_Vacante.objects.get(id=educacion_id)
        educacion_form = EducacionVacanteForm(request.POST, instance=educacion)
        educacion_form.save()
            
        return redirect('/vacante/' + str(vacante_id))

    else:
        educacion = Educacion_Vacante.objects.get(id=educacion_id)
        educacion_form = EducacionVacanteForm(instance=educacion)
        context = {
            'educacion_form': educacion_form,
            'educacion_id': educacion_id,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/modificar/vacante/educacion.html', context)

    return redirect('index')


def eliminar_educacion_vacante(request, vacante_id, educacion_id):
    educacion = Educacion_Vacante.objects.get(id=educacion_id)
    educacion.delete()
    return redirect('/vacante/' + str(vacante_id))


def crear_idioma_vacante(request, vacante_id):
    if request.method == 'POST':
        idioma_form = IdiomaVacanteForm(request.POST)
        idioma = idioma_form.save(commit=False)
        idioma.vacante = Vacante.objects.get(id=vacante_id)
        idioma.save()
            
        return redirect('/vacante/' + str(vacante_id))

    else:
        idioma_form = IdiomaVacanteForm()
        context = {
            'idioma_form': idioma_form,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/agregar/vacante/idioma.html', context)

    return redirect('index')


def modificar_idioma_vacante(request, vacante_id, idioma_id):
    if request.method == 'POST':
        idioma = Idioma_Vacante.objects.get(id=idioma_id)
        idioma_form = IdiomaVacanteForm(request.POST, instance=idioma)
        idioma_form.save()
            
        return redirect('/vacante/' + str(vacante_id))

    else:
        idioma = Idioma_Vacante.objects.get(id=idioma_id)
        idioma_form = IdiomaVacanteForm(instance=idioma)
        context = {
            'idioma_form': idioma_form,
            'idioma_id': idioma_id,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/modificar/vacante/idioma.html', context)

    return redirect('index')


def eliminar_idioma_vacante(request, vacante_id, idioma_id):
    idioma = Idioma_Vacante.objects.get(id=idioma_id)
    idioma.delete()
    return redirect('/vacante/' + str(vacante_id))



def crear_habilidad_vacante(request, vacante_id):
    if request.method == 'POST':
        habilidad_form = HabilidadVacanteForm(request.POST)
        habilidad = habilidad_form.save(commit=False)
        habilidad.vacante = Vacante.objects.get(id=vacante_id)
        habilidad.save()
            
        return redirect('/vacante/' + str(vacante_id))

    else:
        habilidad_form = HabilidadVacanteForm()
        context = {
            'habilidad_form': habilidad_form,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/agregar/vacante/habilidad.html', context)

    return redirect('index')


def modificar_habilidad_vacante(request, vacante_id):
    if request.method == 'POST':
        habilidad_formset = HabilidadVacanteFormSet(request.POST)
        if habilidad_formset.is_valid():
            for habilidad_form in habilidad_formset:
                habilidad = habilidad_form.save(commit=False)
                habilidad.vacante = Vacante.objects.get(id=vacante_id)
                habilidad.save()
                
            return redirect('/vacante/' + str(vacante_id))

    else:
        vacante = Vacante.objects.get(id=vacante_id)
        habilidades = vacante.habilidad_vacante_set.all()
        habilidad_formset = HabilidadVacanteFormSet(queryset=habilidades)
        context = {
            'habilidad_formset': habilidad_formset,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/modificar/vacante/habilidad.html', context)

    return redirect('index')


def eliminar_habilidad_vacante(request, vacante_id, habilidad_id):
    habilidad = Habilidad_Vacante.objects.get(id=habilidad_id)
    habilidad.delete()
    return redirect('/vacante/' + str(vacante_id))


def crear_competencia_vacante(request, vacante_id):
    if request.method == 'POST':
        competencia_form = CompetenciaVacanteForm(request.POST)
        competencia = competencia_form.save(commit=False)
        competencia.vacante = Vacante.objects.get(id=vacante_id)
        competencia.save()
            
        return redirect('/vacante/' + str(vacante_id))

    else:
        competencia_form = CompetenciaVacanteForm()
        context = {
            'competencia_form': competencia_form,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/agregar/vacante/competencia.html', context)


def modificar_competencia_vacante(request, vacante_id):
    if request.method == 'POST':
        competencia_formset = CompetenciaVacanteFormSet(request.POST)
        if competencia_formset.is_valid():
            for competencia_form in competencia_formset:
                competencia = competencia_form.save(commit=False)
                competencia.vacante = Vacante.objects.get(id=vacante_id)
                competencia.save()
                
            return redirect('/vacante/' + str(vacante_id))

    else:
        vacante = Vacante.objects.get(id=vacante_id)
        competencias = vacante.competencia_vacante_set.all()
        competencia_formset = CompetenciaVacanteFormSet(queryset=competencias)
        context = {
            'competencia_formset': competencia_formset,
            'vacante_id': vacante_id,
        }
        return render(request, 'main/registro/modificar/vacante/competencia.html', context)



def eliminar_competencia_vacante(request, vacante_id, competencia_id):
    competencia = Competencia_Vacante.objects.get(id=competencia_id)
    competencia.delete()
    return redirect('/vacante/' + str(vacante_id))


def eliminar_vacante(request, vacante_id):
    vacante = Vacante.objects.get(id=vacante_id)
    vacante.delete()
    return redirect('index')



def lista_vacante(request):
    vacantes = Vacante.objects.all()
    paginator = Paginator(vacantes, 5)

    pagina = request.GET.get('pagina')
    vacante_list = paginator.get_page(pagina)

    context = {
        'vacante_list': vacante_list
    }
    return render(request, 'main/lista/vacante.html', context)


def lista_candidatos(request, vacante_id):
    vacante = Vacante.objects.get(id=vacante_id)
    postulaciones = Postulacion.objects.filter(vacante=vacante)

    paginator = Paginator(postulaciones, 5)

    pagina = request.GET.get('pagina')
    candidatos = paginator.get_page(pagina)

    context = {
        'candidatos': candidatos,
    }
    return render(request, 'main/lista/candidatos.html', context)


def postularse_vacante(request, vacante_id):
    usuario_id = request.session['id']

    habilidad = obtenerHabilidad(usuario_id, vacante_id)
    competencia = obtenerCompetencia(usuario_id, vacante_id)
    idioma = obtenerIdioma(usuario_id, vacante_id)
    educacion = obtenerEducacion(usuario_id, vacante_id)
    experiencia = obtenerExperiencia(usuario_id, vacante_id)
    sexo = obtenerSexo(usuario_id, vacante_id)
    edad = obtenerEdad(usuario_id, vacante_id)

    categoria = obtenerCategoria(habilidad, competencia, idioma, educacion, experiencia, sexo, edad)

    if categoria == 'apto':
        categoria = 'Muy apto'
    elif categoria == 'medio-apto':
        categoria = 'Medio apto'
    else:
        categoria = 'No apto'

    postulacion = Postulacion(
        usuario = Usuario.objects.get(id=usuario_id),
        vacante = Vacante.objects.get(id=vacante_id),
        habilidad = habilidad,
        competencia = competencia,
        idioma = idioma,
        educacion = educacion,
        experiencia = experiencia,
        sexo = sexo,
        edad = edad,
        categoria = categoria,
    )
    postulacion.save()

    return redirect('index')



# FUNCIONES DE PUNTUACIÓN  ---------------------------------
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     WORD = re.compile(r'\w+')
     words = WORD.findall(text)
     return Counter(words)


def obtenerHabilidad(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)
    habilidades_usuario = usuario.habilidad_usuario_set.all()
    habilidades_vacante = vacante.habilidad_vacante_set.all()

    total_de_habilidades = habilidades_vacante.count()
    habilidades_similares = 0

    for habilidad_vacante in habilidades_vacante:
        for habilidad_usuario in habilidades_usuario:
            habilidad1 = text_to_vector(habilidad_vacante.habilidad)
            habilidad2 = text_to_vector(habilidad_usuario.habilidad)
            coseno = get_cosine(habilidad1, habilidad2)
            if coseno >= 0.30:
                habilidades_similares += 1
                break

    return habilidades_similares / total_de_habilidades



def obtenerCompetencia(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)
    competencias_usuario = usuario.competencia_usuario_set.all()
    competencias_vacante = vacante.competencia_vacante_set.all()

    total_de_competencias = competencias_vacante.count()
    competencias_similares = 0

    for competencia_vacante in competencias_vacante:
        for competencia_usuario in competencias_usuario:
            competencia1 = text_to_vector(competencia_vacante.competencia)
            competencia2 = text_to_vector(competencia_usuario.competencia)
            coseno = get_cosine(competencia1, competencia2)
            if coseno >= 0.40:
                competencias_similares += 1
                break

    return competencias_similares / total_de_competencias


def obtenerIdioma(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)
    idiomas_usuario = usuario.idioma_usuario_set.all()
    idiomas_vacante = vacante.idioma_vacante_set.all()

    total_de_idiomas = idiomas_vacante.count()
    idiomas_similares = 0

    for idioma_vacante in idiomas_vacante:
        for idioma_usuario in idiomas_usuario:
            if idioma_vacante.idioma.id == idioma_usuario.idioma.id:
                idiomas_similares += 1
                break

    return idiomas_similares / total_de_idiomas


def obtenerEducacion(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)
    educaciones_usuario = usuario.educacion_usuario_set.all()
    educaciones_vacante = vacante.educacion_vacante_set.all()

    total_de_educaciones = educaciones_vacante.count()
    educaciones_similares = 0

    for educacion_vacante in educaciones_vacante:
        nivel_vacante_id = educacion_vacante.nivel.id
        area_vacante_id = educacion_vacante.area.id

        for educacion_usuario in educaciones_usuario:
            nivel_usuario_id = educacion_usuario.nivel.id
            area_usuario_id = educacion_usuario.area.id

            if area_vacante_id == area_usuario_id:
                educaciones_similares += 0.5
                if nivel_vacante_id == nivel_usuario_id:
                    educaciones_similares += 0.5
                    break

    return educaciones_similares / total_de_educaciones



def obtenerExperiencia(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)

    experiencia_vacante = vacante.años_de_experiencia_minima
    experiencia_usuario = usuario.años_de_experiencia

    experiencia_similar = False

    if experiencia_usuario >= experiencia_vacante:
        experiencia_similar = True

    return experiencia_similar



def obtenerSexo(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)
    sexo_vacante = vacante.sexo.sexo
    sexo_usuario = usuario.sexo.sexo
    sexo_similar = False
    
    if sexo_vacante == sexo_usuario:
        sexo_similar = True
    elif sexo_vacante == "Indiferente":
        sexo_similar = True

    return sexo_similar


def obtenerEdad(usuario_id, vacante_id):
    usuario = Usuario.objects.get(id=usuario_id)
    vacante = Vacante.objects.get(id=vacante_id)

    edad = vacante.edad_set.get()
    edad_usuario = relativedelta(datetime.now(), usuario.fecha_de_nacimiento).years
    edad_minima = edad.minima
    edad_maxima = edad.maxima
    
    edad_similar = False
    if edad_usuario >= edad_minima and edad_usuario <= edad_maxima:
        edad_similar = True

    return edad_similar


def ia(request):
    main_dataset = pd.read_csv('dataset.data', sep= ',', header= None)

    X = main_dataset.values[:, 0:7]
    Y = main_dataset.values[:,7]
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

    settings.clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
    settings.clf.fit(X_train, y_train)

    response = "<b>Filtro IA cargado con éxito.</b><br>"
    response = response + '<b>Precisión en los datos de entrenamiento: </b>' +  str(accuracy_score(y_true=y_train, y_pred=settings.clf.predict(X_train)) * 100) + '%'
    response = response + "<br>"
    response = response + '<b>Precisión en los datos de prueba: </b>' +  str(accuracy_score(y_true=y_test, y_pred=settings.clf.predict(X_test)) * 100) + '%'
    response = response + "<br>"
    response = response + "<a href='/'>Ir a inicio</a>"
    
    return HttpResponse(response)


def obtenerCategoria(habilidad, competencia, idioma, educacion, experiencia, sexo, edad):
    return settings.clf.predict([[habilidad, competencia, idioma, educacion, experiencia, sexo, edad]])

