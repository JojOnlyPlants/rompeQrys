from django import forms
from red_social.models import Usuario, Cuenta

class NombreForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido_paterno', 'apellido_materno']

class ContrasenaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'contrasena']

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'email']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['foto_perfil']