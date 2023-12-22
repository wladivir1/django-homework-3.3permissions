from rest_framework import permissions


  
class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.creator or request.user.is_staff    
    
   