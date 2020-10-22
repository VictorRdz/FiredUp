from django.db import models

# LISTAS ---------------------------------------------
class Sexo(models.Model):
    sexo = models.CharField(max_length=15)
    def __str__(self):
        return self.sexo

class Idioma(models.Model):
    idioma = models.CharField(max_length=20)
    def __str__(self):
        return str(self.idioma)

class Nivel_Educativo(models.Model):
    nivel = models.CharField(max_length=50)
    def __str__(self):
        return self.nivel
    
class Area_Educativa(models.Model):
    area = models.CharField(max_length=50)
    def __str__(self):
        return self.area

class Tipo_Vacante(models.Model):
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.tipo

class Departamento(models.Model):
    departamento = models.CharField(max_length=50)
    def __str__(self):
        return self.departamento

class Frecuencia_Remuneracion(models.Model):
    frecuencia = models.CharField(max_length=10)
    def __str__(self):
        return self.frecuencia



# USUARIO ---------------------------------------------
class Usuario(models.Model):
    correo_electronico = models.EmailField()
    contrasena = models.CharField(max_length=256)
    nombre = models.CharField(max_length=50)
    quien_soy = models.TextField(max_length=640)
    fecha_de_nacimiento = models.DateField()
    años_de_experiencia = models.SmallIntegerField()
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    informacion_adicional = models.TextField(max_length=640)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre



# VACANTE ---------------------------------------------

class Vacante(models.Model):
    puesto = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=400)
    tipo = models.ForeignKey(Tipo_Vacante, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    frecuencia = models.CharField(max_length=80)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    años_de_experiencia_minima = models.SmallIntegerField()
    informacion_adicional = models.TextField(max_length=640)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.puesto


class Remuneracion(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE, default=0)
    frecuencia = models.ForeignKey(Frecuencia_Remuneracion, on_delete=models.CASCADE)
    minima = models.DecimalField(max_digits=22, decimal_places=2)
    maxima = models.DecimalField(max_digits=22, decimal_places=2)
    def __str__(self):
            return ('$' + str(self.minima) + " - $" + str(self.maxima))

class Edad(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE, default=0)
    minima = models.SmallIntegerField()
    maxima = models.SmallIntegerField()
    def __str__(self):
        return ('de ' + str(self.minima) + " a " + str(self.maxima) + ' años.')


# POSTULACION ---------------------------------------------
class Postulacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    habilidad = models.DecimalField(max_digits=3, decimal_places=2)
    competencia = models.DecimalField(max_digits=3, decimal_places=2)
    idioma = models.DecimalField(max_digits=3, decimal_places=2)
    educacion = models.DecimalField(max_digits=3, decimal_places=2)
    experiencia = models.BooleanField()
    sexo = models.BooleanField()
    edad = models.BooleanField()
    categoria = models.CharField(max_length=20, default="")
    def __str__(self):
        return (str(self.vacante) + " - " + str(self.usuario))



# REQUISITOS ---------------------------------------------
class Habilidad_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    habilidad = models.CharField(max_length=60)
    def __str__(self):
        return self.habilidad

class Habilidad_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    habilidad = models.CharField(max_length=60)
    def __str__(self):
        return self.habilidad


class Competencia_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    competencia = models.CharField(max_length=60)
    def __str__(self):
        return self.competencia

class Competencia_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    competencia = models.CharField(max_length=60)
    def __str__(self):
        return self.competencia


class Educacion_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=64)
    institucion = models.CharField(max_length=64)
    nivel = models.ForeignKey(Nivel_Educativo, on_delete=models.CASCADE)
    area = models.ForeignKey(Area_Educativa, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.titulo

class Educacion_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel_Educativo, on_delete=models.CASCADE)
    area = models.ForeignKey(Area_Educativa, on_delete=models.CASCADE)



class Idioma_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)


class Idioma_Vacante(models.Model):
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
