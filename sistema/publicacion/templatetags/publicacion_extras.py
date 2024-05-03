from django import template
from publicacion.models import Publicacion

register = template.Library()

@register.simple_tag
def publicaciones():
    publicaciones = Publicacion.objects.all()
    return publicaciones