from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Creamos un router y registramos nuestros viewsets con él.
router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'lugares', views.LugarViewSet)
router.register(r'profesores', views.ProfesorViewSet)
router.register(r'talleres', views.TallerViewSet)

# Las URLs de la API son ahora determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]
