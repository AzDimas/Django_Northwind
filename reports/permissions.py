from rest_framework.permissions import BasePermission

class HasRole(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        required = getattr(view, "required_roles", None)
        if required is None:
            return True
        profile = getattr(request.user, "profile", None)
        if not profile:
            return False
        return profile.roles.filter(name__in=required).exists()


class HasPermissionCode(BasePermission):
    def has_permission(self, request, view):
        codes = getattr(view, "required_permission_codes", None)
        if not codes:
            return True
        return any(
            request.user.has_perm(f"reports.{code}") for code in codes
        )
