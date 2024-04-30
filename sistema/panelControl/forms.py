from django import forms
from red_social.models import Usuario, Cuenta

class UserForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=100)
    apellido_paterno = forms.CharField(label='Apellido Paterno', max_length=100)
    apellido_materno = forms.CharField(label='Apellido Materno', max_length=100)
    email = forms.EmailField(label='E-mail')

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