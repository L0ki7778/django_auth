from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        is_staff = bool(request.user and request.user.is_staff and request.user.username != "rene")
        return is_staff

class IsAdminForManufacturerDetailAccess(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user and request.user.username == "rene":
            return False
        if  request.method in SAFE_METHODS :
            return True
        if request.method == "DELETE":
            return bool(request.user and request.user.is_superuser)
        else:
            return bool(request.user and request.user.is_staff)

class IsOwnerOrAdminForDetailAccess(BasePermission):

    def has_object_permission(self,request,user,obj):
        # user muss im obj vorhanden sein, um user-permissions zu erstellen
        if request.user == obj.user:
           return bool(request.method != 'DELETE')
        if request.method == 'DELETE':
            return bool(request.user and request.user.is_superuser)
        else:
            return bool(request.user and request.user.is_staff)
