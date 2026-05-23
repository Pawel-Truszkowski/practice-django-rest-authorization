from rest_framework.permissions import BasePermission

from .acl import check_permission

# has_permission — odpowiada na pytanie „czy w ogóle możesz wejść do tego widoku?"
# has_object_permission — odpowiada na pytanie „czy możesz dotknąć tego konkretnego obiektu?"

class NotePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        action_map = {
            'GET': 'read',
            'POST': 'create',
            'PUT': 'update',
            'PATCH': 'update',
            'DELETE': 'delete',
        }
        action = action_map.get(request.method, None)
        
        if action is None:
            return False
        
        return check_permission(request.user, obj, action)
    

