from django.shortcuts import render
from.models import Cuenta,Publicacion,Usuario,Solicitud,Amistad,Bloqueado

# Create your views here.
def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request,"paginas/inicio.html",{'publicaciones':publicaciones})

def bandeja_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "paginas/bandeja_solicitudes.html",{'solicitudes':solicitudes})

def perfil(request):
    return render(request, "paginas/perfil.html")

def busqueda(request):
    return render(request, "paginas/busqueda.html")

def notificaciones(request):
    return render(request, "paginas/notificaciones.html")