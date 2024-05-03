from django.shortcuts import render
from django.views.generic.base import TemplateView

class PaginaInicioView(TemplateView):
    template_name = "paginas/inicio.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'Inicio'})

class PaginaBusquedaView(TemplateView):
    template_name = "paginas/busqueda.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulo': 'Busqueda'})

class PaginaPerfilView(TemplateView):
    template_name = "paginas/perfil.html"
     
    def get(self, request, *args, **kwargs):
         return render(request, self.template_name, {'titulo': 'perfil'})
