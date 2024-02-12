from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # only the owner has access to tasks
        return obj.user == request.user

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
