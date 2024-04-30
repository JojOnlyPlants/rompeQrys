from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from red_social.models import Usuario, Cuenta

from .forms import *

# Esperar a sistema de login para cambiar id por request.user.id
# CAMBIAR LA DEFINICION ACTUAL POR request.user.id HASTA QUE SE IMPLEMENTE EL SISTEMA DE LOGIN, ESTO ES SOLO PARA PRUEBAS
def panel(request, id):
    usuario = Usuario.objects.get(id=id)
    cuenta = usuario.cuenta
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=usuario)
        cuenta_form = CuentaForm(request.POST, request.FILES, instance=cuenta)
        if user_form.has_changed() or cuenta_form.has_changed():
            if user_form.is_valid() and cuenta_form.is_valid():
                user_form.save()
                cuenta_form.save()
                messages.success(request, 'Datos actualizados correctamente')
            else:
                messages.error(request, 'Error al actualizar los datos')
        return redirect('panel', id=usuario.id)
    else:
        user_form = UserForm(instance=usuario)
        cuenta_form = CuentaForm(instance=cuenta)
    return render(request, 'panel.html', {'user_form': user_form, 'cuenta_form': cuenta_form, 'cuenta': cuenta})

def nombre(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = NombreForm(request.POST or None, request.FILES or None , instance=usuario)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Nombre actualizado correctamente')
        return redirect('panel')
    else:
        messages.error(request, 'Error al actualizar el nombre')
    return render(request, 'nombre.html', {'formulario': formulario})

# ESTE METODO FUNCIONA CREANDO UNA NUEVA INSTANCIA DE USUARIO, Y EL CAMBIO SE VE EN EL PANEL DE ADMIN DE DJANGO PERO HASHEADO,
# NO SE PUEDE CAMBIAR AL PARECER
def contrasena(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            usuario.set_password(password)
            usuario.save()
            messages.success(request, 'Contraseña actualizada correctamente')
            return redirect('panel')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect(panel)
    return render(request, 'contrasena.html')

# ME LO DIJO COPILOT, NO SE SI CREERLE AL 100
# ESTE ES UN METODO CON MENOS REFACTORIZACION (MUCHO MENOS) PARA CAMBIAR LA CONTRASEÑA, PERO NO SE VE REFLEJADO EN EL PANEL DE ADMIN DE DJANGO
# SIN EMBARGO ESTOY CASI SEGURO QUE SI FUNCIONA
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
        messages.success(request, 'Correo actualizado correctamente')
        return redirect('panel') 
    else :
        messages.error(request, 'Error al actualizar el correo')
    return render(request, 'correo.html', {'formulario': formulario})

def foto(request, id):
    cuenta = Cuenta.objects.get(usuario__id=id)
    formulario = FotoForm(request.POST or None, request.FILES or None , instance=cuenta)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Foto actualizada correctamente')
        return redirect('panel')
    else:
        messages.error(request, 'Error al actualizar la foto')
    return render(request, 'foto.html', {'formulario': formulario})

