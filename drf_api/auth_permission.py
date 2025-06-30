from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Базовый клас
    """
    required_roles = []

    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and
            hasattr(user, 'role') and
            user.role in self.required_roles
        )

class Author(RolePermission):
    required_roles = ['author']

class User(RolePermission):
    required_roles = ['user']
