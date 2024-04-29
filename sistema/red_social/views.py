from django.shortcuts import render
from.models import Cuenta,Publicacion,Usuario,Solicitud,Amistad,Bloqueado

# Create your views here.
def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request,"paginas/inicio.html",{'publicaciones':publicaciones})

def bandeja_solicitudes(request):
    return render(request, "paginas/bandeja_solicitudes.html")

def perfil(request):
    return render(request, "paginas/perfil.html")

def busqueda(request):
    return render(request, "paginas/busqueda.html")

def notificaciones(request):
    return render(request, "paginas/notificaciones.html")