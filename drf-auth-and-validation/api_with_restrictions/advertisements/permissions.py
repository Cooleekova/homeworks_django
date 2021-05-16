from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Нет прав на совершение операции с заказом'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user
