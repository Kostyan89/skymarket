# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission

from users.managers import UserRole


class Admin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRole.ADMIN


class Owner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
