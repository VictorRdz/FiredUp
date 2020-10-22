from django.db import models

# Create your models here.

# --------------------------------------------------------------------------
# TABLAS COMPARTIDAS

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=80)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Caracter(models.Model):
    caracter = models.CharField(max_length=10)
    def __str__(self):
            return self.caracter


class Idioma(models.Model):
    idioma = models.CharField(max_length=20)
    def __str__(self):
        return self.idioma


class Idioma_Nivel(models.Model):
    nivel = models.CharField(max_length=2)
    def __str__(self):
        return self.nivel


class Area_Educativa(models.Model):
    area = models.CharField(max_length=30)
    def __str__(self):
        return self.area


class Nivel_Educativo(models.Model):
    nivel = models.CharField(max_length=25)
    def __str__(self):
        return self.nivel


class Tamaño_Empresa(models.Model):
    tamaño = models.CharField(max_length=20)
    def __str__(self):
        return self.tamaño


class Estado_Civil(models.Model):
    estado_civil = models.CharField(max_length=20)
    def __str__(self):
        return self.estado_civil


# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# TABLAS DE INICIO DE SESIÓN

class Usuario(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(Estado_Civil, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    contrasena = models.CharField(max_length=256)
    telefono = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    es_hombre = models.BooleanField()
    experiencia = models.SmallIntegerField()
    quien_soy = models.TextField(max_length=640)
    informacion_adicional = models.TextField(max_length=640)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    tamaño = models.ForeignKey(Tamaño_Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    contrasena = models.CharField(max_length=256)
    contacto = models.CharField(max_length=40)
    informacion = models.TextField(max_length=640)
    sitio_web = models.CharField(max_length=40)
    verificado = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# TABLAS DE USUARIO

class Educacion_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel_Educativo, on_delete=models.CASCADE)
    area = models.ForeignKey(Area_Educativa, on_delete=models.CASCADE, default=0)
    titulo = models.CharField(max_length=40)
    institucion = models.CharField(max_length=40)
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __str__(self):
        return self.titulo


class Habilidad_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    habilidad = models.CharField(max_length=60)
    def __str__(self):
        return self.habilidad


class Competencia_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    competencia = models.CharField(max_length=60)
    def __str__(self):
        return self.competencia


class Idioma_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Idioma_Nivel, on_delete=models.CASCADE)
    


class Experiencia_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(max_length=256)
    def __str__(self):
        return self.puesto

# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# TABLAS DE VACANTE

class Departamento(models.Model):
    departamento = models.CharField(max_length=30)
    def __str__(self):
        return self.departamento


class Tipo(models.Model):
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.tipo


class Frecuencia_Vacante(models.Model):
    lunes_entrada = models.TimeField(default="12:00:00")
    lunes_salida = models.TimeField(default="12:00:00")
    martes_entrada = models.TimeField(default="12:00:00")
    martes_salida = models.TimeField(default="12:00:00")
    miercoles_entrada = models.TimeField(default="12:00:00")
    miercoles_salida = models.TimeField(default="12:00:00")
    jueves_entrada = models.TimeField(default="12:00:00")
    jueves_salida = models.TimeField(default="12:00:00")
    viernes_entrada = models.TimeField(default="12:00:00")
    viernes_salida = models.TimeField(default="12:00:00")
    sabado_entrada = models.TimeField(default="12:00:00")
    sabado_salida = models.TimeField(default="12:00:00")
    domingo_entrada = models.TimeField(default="12:00:00")
    domingo_salida = models.TimeField(default="12:00:00")


class Frecuencia_Remuneracion(models.Model):
    frecuencia = models.CharField(max_length=10)
    def __str__(self):
        return self.frecuencia

class Remuneracion_Vacante(models.Model):
    frecuencia = models.ForeignKey(Frecuencia_Remuneracion, on_delete=models.CASCADE)
    minimo = models.DecimalField(max_digits=14, decimal_places=2)
    maximo = models.DecimalField(max_digits=14, decimal_places=2)


class Edad_Vacante(models.Model):
    edad = models.CharField(max_length=20, default="")


class Vacante(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    remuneracion = models.ForeignKey(Remuneracion_Vacante, on_delete=models.CASCADE)
    frecuencia = models.ForeignKey(Frecuencia_Vacante, on_delete=models.CASCADE)
    edad = models.ForeignKey(Edad_Vacante, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=400)
    es_hombre = models.BooleanField()
    experiencia_minima = models.SmallIntegerField()
    informacion_adicional = models.TextField(max_length=640)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fecha_limite = models.DateTimeField()


class Educacion_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel_Educativo, on_delete=models.CASCADE)
    caracter = models.ForeignKey(Caracter, on_delete=models.CASCADE, default=0)
    area = models.ForeignKey(Area_Educativa, on_delete=models.CASCADE, default=0)


class Habilidad_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    habilidad = models.CharField(max_length=60)
    caracter = models.ForeignKey(Caracter, on_delete=models.CASCADE, default=0)


class Competencia_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    competencia = models.CharField(max_length=60)
    caracter = models.ForeignKey(Caracter, on_delete=models.CASCADE, default=0)


class Idioma_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Idioma_Nivel, on_delete=models.CASCADE)
    caracter = models.ForeignKey(Caracter, on_delete=models.CASCADE, default=0)


class Funcion_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    funcion = models.CharField(max_length=60)


class Prestacion_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    prestacion = models.CharField(max_length=60)

# --------------------------------------------------------------------------

class Postulacion(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)