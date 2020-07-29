from rest_framework import permissions

# write your custom permission here


class AdminLevelPermission(permissions.BasePermission):
    """
    this object class will check the user permission
    to perform the BusinessUnit crud operations
    """
    message = 'User do not have the permission.'

    def has_permission(self, request, view):
        if request.user.is_staff and request.user.is_active:
            return True
        else:
            return False
