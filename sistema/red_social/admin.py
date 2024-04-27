from django.contrib import admin
from .models import Cuenta,Publicacion,Usuario,Solicitud,Amistad

# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Publicacion)
admin.site.register(Usuario)
admin.site.register(Solicitud)
admin.site.register(Amistad)