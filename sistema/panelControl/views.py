from django.shortcuts import render
from django.http import HttpResponse
from red_social.models import Usuario, Cuenta
# Create your views here.

#Cuenta.foto_perfil, Usuario.nombre, Usuario.email, Usuario.contrasena

def panel(request):
    return render(request, 'panel.html')

def nombre(request):
    return render(request, 'nombre.html')

def contrasena(request):
    return render(request, 'contrasena.html')

def foto(request):
    return render(request, 'foto.html')

def correo(request):
    return render(request, 'correo.html')