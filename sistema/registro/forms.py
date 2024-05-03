from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cuenta


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        GENERO = (('Masculino','Masculino'),('Femenino','Femenino'),('Otro','Otro'))
        fields = ['nickname', 'foto_perfil', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'genero']
        widgets = {
            'nickname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nickname'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Materno'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'})
        }
        choices = {
            'genero': GENERO
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if 'email' in self.changed_data:
                if User.objects.filter(email=email).exists():
                    raise forms.ValidationError("El email ya está registrado, prueba con otro.")
            return email