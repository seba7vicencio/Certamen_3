"""
URL configuration for talleres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from talleres.views import portal_de_talleres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('talleres.urls')), # Incluimos las URLs de la API
    path('api-auth/', include('rest_framework.urls')), # Para el login/logout de la API
    # REQ01 & REQ08: URL para el portal de vecinos
    path('portal/', portal_de_talleres, name='portal_talleres'),
]
