from rest_framework.permissions import BasePermission


class IsLibrarian(BasePermission):
    """Проверка, является ли пользователь Библиотекарем"""
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Librarian').exists()
