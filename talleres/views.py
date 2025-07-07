from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from datetime import date
from .models import Categoria, Lugar, Profesor, Taller
from .serializers import CategoriaSerializer, LugarSerializer, ProfesorSerializer, TallerSerializer
from .permissions import IsStaffOrReadOnly, TallerPermission

# Create your views here.
# Aquí definiremos la lógica para la API REST.

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar categorías.
    """
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class LugarViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar lugares.
    """
    queryset = Lugar.objects.all().order_by('nombre')
    serializer_class = LugarSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class ProfesorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar profesores.
    """
    queryset = Profesor.objects.all().order_by('nombre_completo')
    serializer_class = ProfesorSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

class TallerViewSet(viewsets.ModelViewSet):
    """
    Taller API endpoint.
    """
    queryset = Taller.objects.all().order_by('-fecha')
    serializer_class = TallerSerializer
    permission_classes = [TallerPermission]
    filterset_fields = ['estado', 'categoria', 'lugar', 'profesor']

    def perform_create(self, serializer):
        # Asigna automáticamente el usuario actual como el creador del taller.
        serializer.save(creado_por=self.request.user)

# REQ01 & REQ08: Vista para el portal de vecinos
def portal_de_talleres(request):
    """
    Renderiza la página del portal público con los talleres disponibles.
    """
    # Obtener todas las categorías para el menú de filtro
    categorias = Categoria.objects.all()
    categoria_seleccionada_id = request.GET.get('categoria')

    # Filtrado base de talleres: estado 'aceptado' y fecha futura o de hoy.
    talleres_visibles = Taller.objects.filter(
        estado='aceptado',
        fecha__gte=date.today()
    )

    # Aplicar filtro de categoría si se seleccionó una
    if categoria_seleccionada_id and categoria_seleccionada_id.isdigit():
        talleres_visibles = talleres_visibles.filter(categoria_id=categoria_seleccionada_id)

    # Preparar el contexto para la plantilla
    contexto = {
        'talleres': talleres_visibles.order_by('fecha'),
        'categorias': categorias,
        'categoria_seleccionada_id': int(categoria_seleccionada_id) if categoria_seleccionada_id and categoria_seleccionada_id.isdigit() else None,
        'titulo_pagina': 'Próximos Talleres Municipales'
    }

    # Renderizar la plantilla HTML con los datos
    return render(request, 'talleres/portal.html', contexto)
