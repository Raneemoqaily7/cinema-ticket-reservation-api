from rest_framework import permissions
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self , request,view ,obj):
         
        if request.method in permissions.SAFE_METHODS:
            return True 

        
        

        return obj.reviewer == request.user

class OwnerOnly (permissions.BasePermission):
    def has_object_permission(self ,request,view ,obj):
        if request.method in permissions.SAFE_METHODS: 
            return obj.author == request.user 
            