from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from red_social.models import Usuario, Cuenta
from .forms import *

# Esperar a sistema de login para cambiar id por request.user.id
def panel(request):
    usuario = Usuario.objects.get(id=1)
    return render(request, 'panel.html', {'usuario': usuario})

def nombre(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = NombreForm(request.POST or None, request.FILES or None , instance=usuario)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Nombre actualizado correctamente')
        return redirect('panel') # Redirige a la pagina de panel, cambiarlo por una pagina de confirmacion
    return render(request, 'nombre.html', {'formulario': formulario})

def contrasena(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            usuario.set_password(password)
            usuario.save()
            return redirect('panel')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'contrasena.html', {})

#def contrasena(request, id):
#    usuario = Usuario.objects.get(id=id)
#    print(f'Usuario: {usuario}')  # Print the Usuario object
#    if request.method == 'POST':
#        password = request.POST.get('password')
#        password_confirmation = request.POST.get('password_confirmation')
#        print(f'Password: {password}, Confirmation: {password_confirmation}')  # Print the password and confirmation
#        if password == password_confirmation:
#            usuario.password = password
#            usuario.save()
#            print('Password updated')  # Print a message when the password is updated
#            return redirect('panel')
#        else:
#            messages.error(request, 'Passwords do not match')
#    return render(request, 'contrasena.html', {})

def correo(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = CorreoForm(request.POST or None, request.FILES or None , instance=usuario)
    if formulario.is_valid():
        formulario.save()
        return redirect('panel') # Redirige a la pagina de panel, cambiarlo por una pagina de confirmacion
    return render(request, 'correo.html', {'formulario': formulario})

def foto(request, id):
    cuenta = Cuenta.objects.get(usuario__id=id)
    formulario = FotoForm(request.POST or None, request.FILES or None , instance=cuenta)
    if formulario.is_valid():
        formulario.save()
        return redirect('panel') # Redirige a la pagina de panel, cambiarlo por una pagina de confirmacion
    return render(request, 'foto.html', {'formulario': formulario})

