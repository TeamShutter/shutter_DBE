from email import message
from rest_framework import permissions

class IsNormalUser(permissions.BasePermission):
    message = "user doesn't have permission to perform this action"
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.groups == 'NormalUser':
            return True
        return False

class IsStudioUser(permissions.BasePermission):
    message = "studio doesn't have permission to perform this action"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups == 'StudioUser':
            return True
        return False

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user

class UserReadOnlyStudioAll(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups == 'NormalUser' or not request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS
        
        return True

class StudioReadOnlyUserAll(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups == 'StudioUser' or not request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS

        return True