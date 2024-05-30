from django.contrib import admin
from .models import Publicacion

# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['cuenta','fecha_creacion']
    search_fields = ['cuenta__usuario']
    list_filter = ['cuenta__usuario']

    class Media:
        css = {
            'all': ('publicacion/css/custom_ckeditor.css',)
        }

admin.site.register(Publicacion, PublicacionAdmin)