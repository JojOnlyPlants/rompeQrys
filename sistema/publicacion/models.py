from django.db import models
from ckeditor.fields import RichTextField
from registro.models import Cuenta

# Create your models here.
class Publicacion(models.Model):
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')
    contenido = RichTextField(verbose_name='Texto')
    imagen = models.ImageField(upload_to='imagenes',verbose_name='Imagen', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.contenido