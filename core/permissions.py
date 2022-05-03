from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """Отключаем токены CSRF для API"""

    def enforce_csrf(self, request):
        return


class BasicAuthMixin:
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = (IsAuthenticated,)
