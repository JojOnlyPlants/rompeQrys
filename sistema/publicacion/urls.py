from django.contrib import admin
from django.urls import path, include
from .views import ListaPublicacionesView, DetallePublicacionView, CrearPublicacionView, EditarPublicacionView, EliminarPublicacionView

urlpatterns = [
    path('', ListaPublicacionesView.as_view(), name='publicaciones'),
    path('<int:pk>/<slug:slug>', DetallePublicacionView.as_view(), name='detalle_publicacion'),
    path('crear/', CrearPublicacionView.as_view(), name='crear_publicacion'),
    path('editar/<int:pk>/', EditarPublicacionView.as_view(), name='editar_publicacion'),
    path('eliminar/<int:pk>/', EliminarPublicacionView.as_view(), name='eliminar_publicacion'),
]