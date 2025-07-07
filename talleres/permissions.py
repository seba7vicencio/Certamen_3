from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Permiso que permite la lectura a cualquier usuario autenticado,
    pero la escritura solo a usuarios que no son parte del staff.
    """
    def has_permission(self, request, view):
        # Permite el acceso de lectura (GET, HEAD, OPTIONS) a cualquier usuario autenticado.
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        # Permite el acceso de escritura solo si el usuario es personal (staff).
        return request.user and request.user.is_staff

class TallerPermission(permissions.BasePermission):
    """
    Permiso personalizado para los talleres.
    - Cualquier usuario autenticado puede ver la lista (GET list) y proponer (POST).
    - Cualquier usuario autenticado puede ver los detalles de un taller (GET detail).
    - Solo el personal (staff) puede editar (PUT, PATCH) o borrar (DELETE) un taller.
    """
    def has_permission(self, request, view):
        # Permite el acceso a cualquier usuario autenticado.
        # La lógica de si puede crear o no se maneja a nivel de objeto o en la vista.
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Permite solicitudes de lectura (GET) para cualquier objeto a cualquier usuario autenticado.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permite solicitudes de escritura (PUT, PATCH, DELETE) solo si el usuario es personal (staff).
        return request.user.is_staff
