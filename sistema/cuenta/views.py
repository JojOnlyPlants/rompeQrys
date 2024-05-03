from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registro.models import Cuenta


# Create your views here.
class CuentaListView(ListView):
    model = Cuenta
    template_name = 'cuenta/cuenta_lista.html'
    paginate_by = 12

class CuentaDetailView(DetailView):
    model = Cuenta
    template_name = 'cuenta/cuenta_detalles.html'
    

    def get_object(self):
        return get_object_or_404(Cuenta, user__username=self.kwargs['username'])
