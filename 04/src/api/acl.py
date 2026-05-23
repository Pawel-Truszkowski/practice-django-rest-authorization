

def check_permission(user, obj, action):
    
    if not user and user.is_authenticated:
        return False
    
    if user.is_superuser:
        return True
    
    if getattr(obj, 'owner', None) is None:
        return False
    
    if action in ('read', 'update', 'delete'):
        return obj.owner == user
    
    return False