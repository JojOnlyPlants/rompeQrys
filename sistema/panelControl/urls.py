from django.urls import path
from . import views

urlpatterns = [
    # deberia de empezar desde el perfil
    path('panel', views.panel, name='panel'),
    path('panel/nombre', views.nombre, name='nombre'),
    path('panel/contrasena', views.contrasena, name='contrasena'),
    path('panel/correo', views.correo, name='correo'),
    path('panel/foto', views.foto, name='foto'),
]
