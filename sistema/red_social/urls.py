from django.urls import path
from .views import PaginaBusquedaView, PaginaInicioView

urlpatterns = [
    path('', PaginaInicioView.as_view(), name='inicio'),
    path('busqueda/', PaginaBusquedaView.as_view(), name='busqueda'),
]
