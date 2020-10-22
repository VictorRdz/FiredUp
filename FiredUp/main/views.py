from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .forms import *
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# ------------------------------------------------------------
# Vistas de inicio.

def index(request):
    return render(request, 'main/otro/home.html', {})

# ------------------------------------------------------------

# ------------------------------------------------------------
# Vistas de registro.

def registro_general(request):
    return render(request, 'main/registro/general.html', {})

def registro_empresa(request):
    tamaño_list = Tamaño_Empresa.objects.all()
    context = {
        'tamaño_list': tamaño_list,
    }
    return render(request, 'main/registro/empresa.html', context)

def registro_usuario(request):
    return render(request, 'main/registro/usuario.html', {})

def iniciar_sesion(request):
    return render(request, 'main/registro/login.html', {})

# ------------------------------------------------------------

def registro_empresa_create(request):
    try:
        correo_electronico = request.POST['correo-electronico']
        contrasena = request.POST['contrasena-uno']

        nombre = request.POST['nombre']
        contacto = request.POST['contacto']
        sitio_web = request.POST['sitio-web']
        tamano = request.POST["tamano"]
        informacion = request.POST['informacion']

        pais = request.POST['name']
        direccion = request.POST['address']
        lat = request.POST['lat']
        lng = request.POST['lng']

    except (KeyError):
        return render(request, '/signup/company', {
            'error_message': "Ha ocurrido un error",
        })
    else:
        ubicacion = Ubicacion(
            nombre = pais,
            direccion = direccion,
            lat = lat,
            lng = lng
        )
        ubicacion.save()
        
        empresa = Empresa(
            ubicacion = ubicacion,
            tamaño = Tamaño_Empresa.objects.get(id=tamano),
            nombre = nombre,
            correo_electronico = correo_electronico,
            contrasena = contrasena,
            contacto = contacto,
            informacion = informacion,
            sitio_web = sitio_web,
            verificado = False,
            created_at = timezone.now(),
            updated_at = timezone.now()
        )
        empresa.save()

        return render(request, 'main/registro/general.html', {})
        #return HttpResponseRedirect(reverse('/signup', args=(empresa.id,)))



def empresa_detalle(request, empresa_id):
    empresa = Empresa.objects.get(id=empresa_id)
    vacante_list = Vacante.objects.filter(empresa=empresa)
    context =  {
        'empresa': empresa,
        'vacante_list': vacante_list,
    }
    return render(request, 'main/detalle/empresa.html', context)



def registro_vacante(request):
    departamento_list = Departamento.objects.all()
    tipo_list = Tipo.objects.all()
    frecuencia_remuneracion_list = Frecuencia_Remuneracion.objects.all()
    nivel_educativo_list = Nivel_Educativo.objects.all()
    area_educativa_list = Area_Educativa.objects.all()
    idioma_list = Idioma.objects.all()
    idioma_nivel_list = Idioma_Nivel.objects.all()
    caracter_list = Caracter.objects.all()
    edad_list = Edad_Vacante.objects.all()
    habilidad_formset = Habilidad_Vacante_FormSet
    competencia_formset = Competencia_Vacante_FormSet
    idioma_formset = Idioma_Vacante_FormSet
    educacion_formset = Educacion_Vacante_FormSet
    funcion_formset = Funcion_Vacante_FormSet
    prestacion_formset = Prestacion_Vacante_FormSet
    remuneracion_formset = Remuneracion_Vacante_FormSet

    context = {
        'departamento_list': departamento_list,
        'tipo_list': tipo_list,
        'frecuencia_remuneracion_list': frecuencia_remuneracion_list,
        'nivel_educativo_list': nivel_educativo_list,
        'area_educativa_list': area_educativa_list,
        'idioma_list': idioma_list,
        'idioma_nivel_list': idioma_nivel_list,
        'caracter_list': caracter_list,
        'edad_list': edad_list,
        'habilidad_formset': habilidad_formset,
        'competencia_formset': competencia_formset,
        'idioma_formset': idioma_formset,
        'educacion_formset': educacion_formset,
        'funcion_formset': funcion_formset,
        'prestacion_formset': prestacion_formset,
        'remuneracion_formset': remuneracion_formset,
    }

    return render(request, 'main/registro/vacante.html', context)


def registro_vacante_create(request):
    try:
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        area_id = request.POST['area-puesto']
        tipo_id = request.POST['tipo-puesto']
        edad = request.POST['edad']
        sexo = request.POST['sexo']
        experiencia = request.POST['experiencia']
        informacion_adicional = request.POST['informacion-adicional']

        name = request.POST['name']
        address = request.POST['address']
        lat = request.POST['lat']
        lng = request.POST['lng']

        lunes_in = request.POST['lunes-in']
        lunes_out = request.POST['lunes-out']
        martes_in = request.POST['martes-in']
        martes_out = request.POST['martes-out']
        miercoles_in = request.POST['miercoles-in']
        miercoles_out = request.POST['miercoles-out']
        jueves_in = request.POST['jueves-in']
        jueves_out = request.POST['jueves-out']
        viernes_in = request.POST['viernes-in']
        viernes_out = request.POST['viernes-out']
        sabado_in = request.POST['sabado-in']
        sabado_out = request.POST['sabado-out']
        domingo_in = request.POST['domingo-in']
        domingo_out = request.POST['domingo-out']
        
        remuneracion_vacante = Remuneracion_Vacante_FormSet(request.POST)
        funciones = Funcion_Vacante_FormSet(request.POST)
        prestaciones = Prestacion_Vacante_FormSet(request.POST)
        educaciones = Educacion_Vacante_FormSet(request.POST)
        idiomas = Idioma_Vacante_FormSet(request.POST)
        habilidades = Habilidad_Vacante_FormSet(request.POST)
        competencias = Competencia_Vacante_FormSet(request.POST)

    except (KeyError):
        return render(request, '/signup/company', {
            'error_message': "Ha ocurrido un error",
        })
    else:
        empresa_id = request.session.user_id
        # Datos necearios para crear la vacante primero
        frecuencia_vacante = Frecuencia_Vacante(
            lunes_entrada = lunes_in,
            lunes_salida = lunes_out,
            martes_entrada = martes_in,
            martes_salida = martes_out,
            miercoles_entrada = miercoles_in,
            miercoles_salida = miercoles_out,
            jueves_entrada = jueves_in,
            jueves_salida = jueves_out,
            viernes_entrada = viernes_in,
            viernes_salida = viernes_out,
            sabado_entrada = sabado_in,
            sabado_salida = sabado_out,
            domingo_entrada = domingo_in,
            domingo_salida = domingo_out
        )
        frecuencia_vacante.save()

        ubicacion_vacante = Ubicacion(
            nombre = name,
            direccion = address,
            lat = lat,
            lng = lng
        )
        ubicacion_vacante.save()

        remuneracion_id = 0;
        if remuneracion_vacante.is_valid():
            r = remuneracion_vacante[0].save()
            remuneracion_id = r.id

        #return HttpResponse(edad)
        vacante = Vacante(
            tipo = Tipo.objects.get(id=tipo_id),
            ubicacion = Ubicacion.objects.get(id=ubicacion_vacante.id),
            empresa = Empresa.objects.get(id=empresa_id),
            departamento = Departamento.objects.get(id=area_id),
            remuneracion = Remuneracion_Vacante.objects.get(id=remuneracion_id),
            frecuencia = Frecuencia_Vacante.objects.get(id=frecuencia_vacante.id),
            edad = Edad_Vacante.objects.get(id=edad),
            puesto = titulo,
            descripcion = descripcion,
            es_hombre = sexo,
            experiencia_minima = experiencia,
            informacion_adicional = informacion_adicional,
            created_at = timezone.now(),
            updated_at = timezone.now(),
            fecha_limite = timezone.now(),
        )
        vacante.save()
        
        for funcion in funciones:
            if funcion.has_changed() and funcion.is_valid():
                f = funcion.save(commit=False)
                f.vacante = Vacante.objects.get(id=vacante.id)
                f.save()

        for prestacion in prestaciones:
            if prestacion.has_changed() and prestacion.is_valid():
                p = prestacion.save(commit=False)
                p.vacante = Vacante.objects.get(id=vacante.id)
                p.save()

        for educacion in educaciones:
            if educacion.has_changed() and educacion.is_valid():
                e = educacion.save(commit=False)
                e.vacante = Vacante.objects.get(id=vacante.id)
                e.save()

        for idioma in idiomas:
            if idioma.has_changed() and idioma.is_valid():
                i = idioma.save(commit=False)
                i.vacante = Vacante.objects.get(id=vacante.id)
                i.save()

        for habilidad in habilidades:
            if habilidad.has_changed() and habilidad.is_valid():
                h = habilidad.save(commit=False)
                h.vacante = Vacante.objects.get(id=vacante.id)
                h.save()

        for competencia in competencias:
            if competencia.has_changed() and competencia.is_valid():
                c = competencia.save(commit=False)
                c.vacante = Vacante.objects.get(id=vacante.id)
                c.save()

        return redirect('/vacante/' + str(vacante.id))


def vacante_detalle(request, vacante_id):
    vacante = Vacante.objects.get(id=vacante_id)
    funcion_list = Funcion_Vacante.objects.filter(vacante=vacante_id)
    prestacion_list = Prestacion_Vacante.objects.filter(vacante=vacante_id)
    educacion_list = Educacion_Vacante.objects.filter(vacante=vacante_id)
    idioma_list = Idioma_Vacante.objects.filter(vacante=vacante_id)
    habilidad_list = Habilidad_Vacante.objects.filter(vacante=vacante_id)
    competencia_list = Competencia_Vacante.objects.filter(vacante=vacante_id)

    context = {
        'vacante': vacante,
        'funcion_list': funcion_list,
        'prestacion_list': prestacion_list,
        'educacion_list': educacion_list,
        'idioma_list': idioma_list,
        'habilidad_list': habilidad_list,
        'competencia_list': competencia_list,
    }
    return render(request, 'main/detalle/vacante.html', context)


def vacante_borrar(request, vacante_id):
    vacante = Vacante.objects.get(id=vacante_id)
    vacante.delete()
    return redirect('/admin')


def login_enter(request):
    correo_electronico = request.POST['correo-electronico']
    contrasena = request.POST['contrasena']
    try:
        usuario = Usuario.objects.get(correo_electronico=correo_electronico)
    except Usuario.DoesNotExist:
        usuario = None
    else:
        if usuario.contrasena == contrasena:
            request.session['user_type'] = "Usuario"
            request.session['user_name'] = usuario.nombre
            request.session['user_id'] = usuario.id
            request.session.set_expiry(0)
            return redirect('/user/' + str(usuario.id))

    try:
        empresa = Empresa.objects.get(correo_electronico=correo_electronico)
    except Empresa.DoesNotExist:
        empresa = None
    else:
        if empresa.contrasena == contrasena:
            request.session['user_type'] = "Empresa"
            request.session['user_name'] = empresa.nombre
            request.session['user_id'] = empresa.id
            request.session.set_expiry(0)
            return redirect('/company/' + str(empresa.id))

    return redirect('/login')
 

def cerrar_sesion(request):
    request.session.flush()
    return redirect('/')


def buscar(request):
    vacante_list = Vacante.objects.all()
    context = {
        'vacante_list': vacante_list,
    }
    return render(request, 'main/otro/buscar.html', context)

def usuario_detalle(request, usuario_id):
    return render(request, 'main/detalle/usuario.html', {})