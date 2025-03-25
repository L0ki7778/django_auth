from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        is_staff = bool(request.user and request.user.is_staff and request.user.username != "rene")
        return is_staff
