from django.urls import path
from .views import PaginaBusquedaView, PaginaInicioView, PaginaPerfilView

urlpatterns = [
    path('', PaginaInicioView.as_view(), name='inicio'),
    path('busqueda/', PaginaBusquedaView.as_view(), name='busqueda'),
    path('perfil/',  PaginaPerfilView.as_view(), name='perfil')
]
