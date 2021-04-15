from rest_framework import permissions


class IsAuthenticatedConfirmed(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_email_confirmed
