from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('bandeja_solicitudes', views.bandeja_solicitudes, name='bandeja_solicitudes'),
    path('perfil', views.perfil, name='perfil'),
    path('busqueda', views.busqueda, name='busqueda'),
    path('notificaciones', views.notificaciones, name='notificaciones'),
    path('rechazar_solicitud/<str:cuenta_solicitante>/<str:cuenta_a_solicitar>', views.rechazar_solicitud, name='rechazar_solicitud'),
]
