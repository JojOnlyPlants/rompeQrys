from django.shortcuts import render,redirect
from.models import Cuenta,Publicacion,Usuario,Solicitud,Amistad,Bloqueado

# Create your views here.
def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request,"paginas/inicio.html",{'publicaciones':publicaciones})

def bandeja_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "paginas/bandeja_solicitudes.html",{'solicitudes':solicitudes})

def rechazar_solicitud(request,cuenta_solicitante,cuenta_a_solicitar):
    solicitud = Solicitud.objects.get(cuenta_solicitante=cuenta_solicitante,cuenta_a_solicitar=cuenta_a_solicitar)
    solicitud.delete()
    return redirect('bandeja_solicitudes')

def aceptar_solicitud(request,cuenta_solicitante,cuenta_a_solicitar):
    solicitud = Solicitud.objects.get(cuenta_solicitante=cuenta_solicitante,cuenta_a_solicitar=cuenta_a_solicitar)
    cuenta_solicitante = Cuenta.objects.get(nickname=solicitud.cuenta_solicitante)
    cuenta_a_solicitar = Cuenta.objects.get(nickname=solicitud.cuenta_a_solicitar)
    amistad = Amistad(cuenta_1=cuenta_solicitante,cuenta_2=cuenta_a_solicitar)
    amistad.save()
    solicitud.delete()
    return redirect('bandeja_solicitudes')

def perfil(request):
    return render(request, "paginas/perfil.html")

def busqueda(request):
    return render(request, "paginas/busqueda.html")

def notificaciones(request):
    return render(request, "paginas/notificaciones.html")