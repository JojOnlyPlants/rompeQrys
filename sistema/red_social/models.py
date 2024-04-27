from django.db import models

# Create your models here.
class Cuenta(models.Model):
    nickname = models.CharField(max_length=50,verbose_name='Nickname')
    foto_perfil = models.ImageField(upload_to='fotos_perfil',verbose_name='Foto de perfil')

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['nickname']
    
    def __str__(self):
        return self.nickname

class Publicacion(models.Model):
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')
    texto = models.TextField(max_length=1000,verbose_name='Texto')
    imagen = models.ImageField(upload_to='imagenes',verbose_name='Imagen')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
    
    def __str__(self):
        return self.texto
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=50,verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=50,verbose_name='Apellido materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    genero = models.CharField(max_length=15,verbose_name='Género')
    email = models.EmailField(verbose_name='Email')
    contrasena = models.CharField(max_length=50,verbose_name='Contraseña')
    es_administrador = models.BooleanField(default=False,verbose_name='Es administrador')
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['cuenta']
    
    def __str__(self):
        return self.cuenta.nickname
    
class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name='Usuario')
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
    
    def __str__(self):
        return self.usuario.cuenta.nickname
    
class Amistad(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name='Usuario')
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')

    class Meta:
        verbose_name = 'Amistad'
        verbose_name_plural = 'Amistades'
    
    def __str__(self):
        return self.usuario.cuenta.nickname

class Bloqueado(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name='Usuario')
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,verbose_name='Cuenta')

    class Meta:
        verbose_name = 'Bloqueado'
        verbose_name_plural = 'Bloqueados'
    
    def __str__(self):
        return self.usuario.cuenta.nickname