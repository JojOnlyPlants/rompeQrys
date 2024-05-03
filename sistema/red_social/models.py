from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su Cuenta enlazada")

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'fotos_perfil/' + filename

# Create your models here.
class Cuenta(models.Model):
    GENERO = (('Masculino','Masculino'),('Femenino','Femenino'),('Otro','Helicoptero Apache'))
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    nickname = models.CharField(max_length=50, verbose_name='Nickname', null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil',verbose_name='Foto de perfil', null=True, blank=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=True, blank=True)
    apellido_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno', null=True, blank=True)
    apellido_materno = models.CharField(max_length=50, verbose_name='Apellido materno', null=True, blank=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    genero = models.CharField(max_length=25, verbose_name='Género', choices=GENERO, null=True, blank=True)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['nickname']
    
    def __str__(self):
        return self.nickname

class Publicacion(models.Model):
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')
    texto = models.TextField(max_length=1000,verbose_name='Texto')
    imagen = models.ImageField(upload_to='imagenes',verbose_name='Imagen', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.texto
    
class Solicitud(models.Model):
    cuenta_solicitante = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta solicitante',related_name='cuenta_solicitante')
    cuenta_a_solicitar = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta a solicitar',related_name='cuenta_a_solicitar')

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
    
    def __str__(self):
        return self.cuenta_solicitante.nickname + ' solicita amistad a ' + self.cuenta_a_solicitar.nickname
    
class Amistad(models.Model):
    cuenta_1 = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta amigo 1',related_name='cuenta_1')
    cuenta_2 = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta amigo 2',related_name='cuenta_2')

    class Meta:
        verbose_name = 'Amistad'
        verbose_name_plural = 'Amistades'
    
    def __str__(self):
        return self.cuenta_1.nickname + ' es amigo de ' + self.cuenta_2.nickname

class Bloqueado(models.Model):
    cuenta_bloqueadora = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta Bloqueadora',related_name='cuenta_bloqueadora')
    cuenta_bloqueada = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta Bloqueada',related_name='cuenta_bloqueada')

    class Meta:
        verbose_name = 'Bloqueado'
        verbose_name_plural = 'Bloqueados'
    
    def __str__(self):
        return self.cuenta_bloqueadora.nickname + ' bloqueo a ' + self.cuenta_bloqueada.nickname
