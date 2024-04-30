from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.panel, name='panel'),
    path('panel/nombre', views.nombre, name='nombre'),
    path('panel/contrasena', views.contrasena, name='contrasena'),
    path('panel/correo', views.correo, name='correo'),
    path('panel/foto', views.foto, name='foto'),
    path('panel/nombre/<int:id>', views.nombre, name='nombre'),
    path('panel/contrasena/<int:id>', views.contrasena, name='contrasena'), 
    path('panel/correo/<int:id>', views.correo, name='correo'),
    path('panel/foto/<int:id>', views.foto, name='foto'),
]
