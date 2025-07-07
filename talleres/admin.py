from django.contrib import admin
from .models import Taller, Categoria, Lugar, Profesor

# REQ02: Registrar modelos para que sean administrables en el Django Admin
admin.site.register(Taller)
admin.site.register(Categoria)
admin.site.register(Lugar)
admin.site.register(Profesor)
