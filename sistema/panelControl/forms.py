from django import forms
from red_social.models import Usuario, Cuenta

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido_paterno', 'apellido_materno', 'email']

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['foto_perfil']
        widgets = {
            'foto_perfil': forms.FileInput(attrs={'class': 'account-settings-fileinput'}),
        }

class NombreForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido_paterno', 'apellido_materno']

class ContrasenaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'password']

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'email']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['foto_perfil']