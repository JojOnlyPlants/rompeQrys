from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['contenido','imagen']
        labels = {
            'contenido':'Texto',
            'imagen':'Imagen'
        }
        widgets = {
            'contenido': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe algo...'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'})
        }

        