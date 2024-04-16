from rest_framework.permissions import BasePermission


class IsActivate(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_active
