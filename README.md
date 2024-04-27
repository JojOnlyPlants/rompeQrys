# Hipopótamos Locos
## Ingeniería de Software
### *Profesores: *
* Ruelas Milanés Daniel
* Manjarrez Angeles Valeria Fernanda
* Escamilla Soto Cristopher Alejandro
---
### *Integrantes del equipo: *
* López Hernández Jesús Haans
* Hernández Rodríguez Oscar David
* Ruiz Reyes Luis Jorge
* Vázquez Torrijos Damián
* Ortega Venegas Rodrigo Aldair
---
## Este Repositorio se va a utilizar para el trabajo en la asignatura de Ingenieria de Software para registrar entregables y control de versiones del equipo 1 "Hipopotamos Locos"


## Iniciar el proyecto

### Instalacion de Python

primero se debe contar con python instalado en la computadora, si no se tiene se puede descargar de la pagina oficial de python https://www.python.org/downloads/

### Instalacion entorno virtual

una vez instalado python se debe instalar el entorno virtual con el siguiente comando
>Nota el comando pip y python pueden cambiar por pip3 y python3 dependiendo del sistema operativo.

```
pip install virtualenv
```

una vez instalado el entorno virtual en la raiz del proyecto se debe crear el entorno virtual con el siguiente comando

```
virtualenv venv
```

una vez creado el entorno virtual se debe activar con el siguiente comando.

```
source venv/bin/activate
```

#### Instalacion de dependencias

una vez activado el entorno virtual se deben instalar las dependencias del proyecto con los siguientes comandos.
> Nota: se deben instalar las dependencias dentro del entorno virtual.

``` 
pip install Django
pip install djangorestframework
pip install PyMySQL
pip install pillow
pip install django-ckeditor
pip install pylint
pip install pylint-django
pip install pylint-celery
```
en caso de contar con pipenv se puede seguir las siguientes instrucciones.

//////////////////// PYTHON  ENV///////////////////////
Crear una nueva carpeta, la cual sera el contenedor de nuestro 
ambiente virtual de python.
```
mkdir Projecto
cd Projecto
```
Crear un ambiente virtual
Con la version de python que tienes instalada, en mi caso es python 3.12
```
pipenv --python 3.12 
```
Esto creara un ambientevirtua alojando en tu pc, la ruta sera especificada
en la consola, ahi estaran todas las intalaciones que se hagan en ese ambiente
Puedes consultarlo tambien con:
```
pipenv --venv
```
Recuerden que para usar este ambien deben estar posicionados siempre en la carpeta que usaron como contenedor, pueden ver lo que hay instalado en su ambien usando:
```
pipenv run pip list
```
Para instalar o desisnstalar cualquier paquete:
```
pipenv install "package"
pipenv uninstall "package"
```
Para eliminar el ambiente:
```
pipenv --rm
```
Despues puede eliminar el contenedor y listo, se habra desinstalado completamente el ambiente.

#### Instalacion de dependencias

///////////////////// CONFIGURACION DEL AMBIENTE //////////////////
Intala en tu ambiente lo siguiente:
```
pipenv install django django-ckeditor djangorestframework PyMySQL
pipenv install Pillow pylint pylint-django pylint-celery
```
Verifica con 
```
pipenv run pip list
```

### Correr el servidor

una vez instaladas las dependencias dentro del ambiente virtual se debe correr el servidor con el siguiente comando dentro de la carpeta donde se encuentra el archivo `manage.py`.

```
python manage.py runserver
```

### Migraciones
Django nos indica que no se han hecho las migraciones correspondiente, esto es por que un proyecto creado en Django crea por defecto una base con tablas predefinidas para cargarlas al projecto, debemos ejecutar:
```
python manage.py migrate
```
Cuando trabajes con modelos, siempre debes indicar que cree las migraciones correspondientes
```
python manage.py makemigrations "nombre de la app"
```
Y luego las aplicamos con:
```
python manage.py migrate
```
### Crear un superusuario
Para usar la interfaz de administrador antes se debe activar con:
```
python manage.py createsuperuser
```

Esto nos pedira un usuario y contrasenia la cual sera la forma de acceder al cliente Admin. usando la ruta:
```
localhost:8000/admin
```

