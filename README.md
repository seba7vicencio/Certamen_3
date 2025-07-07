Sistema de Gestión de Talleres - Municipalidad de Villa Verde

Este proyecto es un sistema web desarrollado con Django y Django REST Framework para gestionar los talleres comunitarios de la Municipalidad de Villa Verde


Tecnologías Utilizadas

- Python 3
- Django
- Django REST Framework
- django-filter
- SQLite 




Instalación y Puesta en Marcha

Sigue estos pasos para instalar y correr el proyecto:


1. Clonar el Repositorio

git clone https://github.com/seba7vicencio/Certamen_3.git


2. Crear y Activar un Entorno Virtual


Crear el entorno
python -m venv ambiente_talleres

Activar en Windows
.\ambiente_talleres\Scripts\activate

3. Instalar las Dependencias
Instala las librerías necesarias con pip.

pip install django djangorestframework django-filter


4. Aplicar las Migraciones
Esto creará la base de datos y sus tablas a partir de los modelos.

Navega a la carpeta que contiene manage.py
cd talleres

python manage.py migrate


5. Ejecutar el Servidor
¡Todo listo para lanzar la aplicación!

python manage.py runserver




Cómo Usar el Sistema


Una vez que el servidor esté corriendo, puedes interactuar con los diferentes componentes:

Portal de Vecinos:
URL: http://127.0.0.1:8000/portal/
Acceso: Público, no requiere inicio de sesión.


Panel de Administración :
URL: http://127.0.0.1:8000/admin/
Acceso: Inicia sesión con el superusuario que creaste o con una cuenta de funcionario (is_staff=True).


API REST :
URL: http://127.0.0.1:8000/api/talleres/
Acceso: Inicia sesión a través de la API (botón 'Log in' en la esquina superior derecha) con una cuenta de Junta de Vecinos (is_staff=False).

Cuentas de Usuario

El proyecto incluye una base de datos (`db.sqlite3`) con usuarios pre-cargados para cada rol. Para la evaluación, utilice las siguientes credenciales:

Administrador (is_superuser=True):
Usuario: admin
Contraseña: admin

Funcionario Municipal (is_staff=True):
Usuario: funcionario
Contraseña: 1234fun987

Junta de Vecinos (is_staff=False):
Usuario: junta_vecinos
Contraseña: vecinos1234
