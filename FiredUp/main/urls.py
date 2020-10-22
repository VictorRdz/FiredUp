from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.registro_general, name='registro_general'),
    path('signup/company/', views.registro_empresa, name='registro_empresa'),
    path('signup/company/create', views.registro_empresa_create, name='registro_empresa_create'),
    path('signup/user/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('login/enter', views.login_enter, name='login_enter'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('buscar/', views.buscar, name='buscar'),
    path('usuario/<int:usuario_id>/', views.usuario_detalle, name='usuario_detalle'),
    
    path('company/<int:empresa_id>/', views.empresa_detalle, name='empresa_detalle'),
    path('vacante/<int:vacante_id>/', views.vacante_detalle, name='vacante_detalle'),
    path('vacante/<int:vacante_id>/delete', views.vacante_borrar, name='vacante_borrar'),
    path('vacante/crear/', views.registro_vacante, name='registro_vacante'),
    path('vacante/crear/create', views.registro_vacante_create, name='registro_vacante_create'),
]