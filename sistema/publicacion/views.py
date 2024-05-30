from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Publicacion
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import PublicacionForm

# Create your views here.

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    
class ListaPublicacionesView(ListView):
    model = Publicacion
    

class DetallePublicacionView(DetailView):
    model = Publicacion



class CrearPublicacionView(CreateView):
    model = Publicacion
    form_class = PublicacionForm
    
    def get_success_url(self):
        return reverse('publicacion')
    

class EditarPublicacionView(UpdateView):
    model = Publicacion
    fields = ['contenido','imagen']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id])+ '?ok'
    

class EliminarPublicacionView(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('publicaciones')