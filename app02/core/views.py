from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from pages.models import Page



@method_decorator(login_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    fields = ['field1', 'field2']  # Reemplaza 'field1', 'field2' con los campos de tu modelo
    template_name = 'core/page_create.html'  # Reemplaza con el nombre de tu plantilla

@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"2da Pagina Web", 'user': request.user})

@method_decorator(login_required, name='dispatch')
class SamplePageView(TemplateView):
    template_name = "core/sample.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})
    

def feed(request):
    return render(request, 'pages/feed.html')