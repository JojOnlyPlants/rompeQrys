from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
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

# TODO CAMBIOS HECHOS, CAMBIE EXTENSIVAMENTE LA BASE DE DATOS, CREE UN USUARIO PERSONALIZADO QUE SOBRERESCRIBE EL USUARIO DE DJANGO
# CON QUE OBJETIVO? PARA PODER VER EL CAMBIO DE CONTRASEÑA EN EL PANEL DE ADMIN DE DJANGO, CON EL OTRO NO SE PODIA HACER
# SIN EMBARGO AHORA LOS CAMBIOS DE CONTRASEÑA SE VEN HASHEADOS EN LA BASE DE DATOS, NO SE SI ESO SEA UN PROBLEMA

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(max_length=50, verbose_name='Apellido materno')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    genero = models.CharField(max_length=15, verbose_name='Género')
    email = models.EmailField(verbose_name='Email', unique=True)
    password = models.CharField(max_length=128)
    es_administrador = models.BooleanField(default=False, verbose_name='Es administrador')
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, verbose_name='Cuenta')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'genero']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['cuenta']

    def __str__(self):
        return self.cuenta.nickname
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="usuario_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="usuario_user_permissions",
        related_query_name="user",
    )

    objects = UsuarioManager()
    
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