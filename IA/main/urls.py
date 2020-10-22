from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Inicio y cierre de sesión
    path('salir', views.cerrar_sesion, name='cerrar_sesion'),
    path('login', views.iniciar_sesion, name='iniciar_sesion'),

    # URLS de usuario
    path('usuario', views.lista_usuario, name='lista_usuario'),
    path('usuario/crear', views.crear_usuario, name='crear_usuario'),
    path('usuario/<int:usuario_id>', views.detalle_usuario, name='detalle_usuario'),
    path('usuario/<int:usuario_id>/modificar', views.modificar_usuario, name='modificar_usuario'),
    path('usuario/<int:usuario_id>/eliminar', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuario/<int:usuario_id>/educacion/crear', views.crear_educacion_usuario, name='crear_educacion_usuario'),
    path('usuario/<int:usuario_id>/educacion/<int:educacion_id>', views.modificar_educacion_usuario, name='modificar_educacion_usuario'),
    path('usuario/<int:usuario_id>/educacion/<int:educacion_id>/eliminar', views.eliminar_educacion_usuario, name='eliminar_educacion_usuario'),
    path('usuario/<int:usuario_id>/habilidad/crear', views.crear_habilidad_usuario, name='crear_habilidad_usuario'),
    path('usuario/<int:usuario_id>/habilidad/modificar', views.modificar_habilidad_usuario, name='modificar_habilidad_usuario'),
    path('usuario/<int:usuario_id>/habilidad/<int:habilidad_id>/eliminar', views.eliminar_habilidad_usuario, name='eliminar_habilidad_usuario'),
    path('usuario/<int:usuario_id>/competencia/crear', views.crear_competencia_usuario, name='crear_competencia_usuario'),
    path('usuario/<int:usuario_id>/competencia/modificar', views.modificar_competencia_usuario, name='modificar_competencia_usuario'),
    path('usuario/<int:usuario_id>/competencia/<int:competencia_id>/eliminar', views.eliminar_competencia_usuario, name='eliminar_competencia_usuario'),
    path('usuario/<int:usuario_id>/idioma/crear', views.crear_idioma_usuario, name='crear_idioma_usuario'),
    path('usuario/<int:usuario_id>/idioma/<int:idioma_id>', views.modificar_idioma_usuario, name='modificar_idioma_usuario'),
    path('usuario/<int:usuario_id>/idioma/<int:idioma_id>/eliminar', views.eliminar_idioma_usuario, name='eliminar_idioma_usuario'),

    #URLS de vacante
    path('vacante', views.lista_vacante, name='lista_vacante'),
    path('vacante/crear', views.crear_vacante, name='crear_vacante'),
    path('vacante/<int:vacante_id>', views.detalle_vacante, name='detalle_vacante'),
    path('vacante/<int:vacante_id>/eliminar', views.eliminar_vacante, name='eliminar_vacante'),
    path('vacante/<int:vacante_id>/educacion/crear', views.crear_educacion_vacante, name='crear_educacion_vacante'),
    path('vacante/<int:vacante_id>/educacion/<int:educacion_id>', views.modificar_educacion_vacante, name='modificar_educacion_vacante'),
    path('vacante/<int:vacante_id>/educacion/<int:educacion_id>/eliminar', views.eliminar_educacion_vacante, name='eliminar_educacion_vacante'),
    path('vacante/<int:vacante_id>/habilidad/crear', views.crear_habilidad_vacante, name='crear_habilidad_vacante'),
    path('vacante/<int:vacante_id>/habilidad/modificar', views.modificar_habilidad_vacante, name='modificar_habilidad_vacante'),
    path('vacante/<int:vacante_id>/habilidad/<int:habilidad_id>/eliminar', views.eliminar_habilidad_vacante, name='eliminar_habilidad_vacante'),
    path('vacante/<int:vacante_id>/competencia/crear', views.crear_competencia_vacante, name='crear_competencia_vacante'),
    path('vacante/<int:vacante_id>/competencia/modificar', views.modificar_competencia_vacante, name='modificar_competencia_vacante'),
    path('vacante/<int:vacante_id>/competencia/<int:competencia_id>/eliminar', views.eliminar_competencia_vacante, name='eliminar_competencia_vacante'),
    path('vacante/<int:vacante_id>/idioma/crear', views.crear_idioma_vacante, name='crear_idioma_vacante'),
    path('vacante/<int:vacante_id>/idioma/<int:idioma_id>', views.modificar_idioma_vacante, name='modificar_idioma_vacante'),
    path('vacante/<int:vacante_id>/idioma/<int:idioma_id>/eliminar', views.eliminar_idioma_vacante, name='eliminar_idioma_vacante'),

    #URLS de postulacion
    path('vacante/<int:vacante_id>/candidatos', views.lista_candidatos, name='lista_candidatos'),
    path('vacante/<int:vacante_id>/postularse', views.postularse_vacante, name='postularse_vacante'),


    path('ia', views.ia, name='ia'),
]