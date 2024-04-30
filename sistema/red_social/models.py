from django.db import models

# Create your models here.
class Cuenta(models.Model):
    nickname = models.CharField(max_length=50,primary_key=True,verbose_name='Nickname')
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
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=50, verbose_name='Apellido materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    genero = models.CharField(max_length=15, verbose_name='Género')
    email = models.EmailField(verbose_name='Email')
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña')
    es_administrador = models.BooleanField(default=False, verbose_name='Es administrador')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name='Cuenta')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['cuenta']

    def _str_(self):
        return self.cuenta.nickname
    
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
