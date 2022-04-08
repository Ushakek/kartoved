from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework import status
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    renderer_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.utils import error_as_dict
from users.forms import UserRegistrationRequestForm


@api_view(['GET'])
@ensure_csrf_cookie
def __init__(request):
    return Response({'init': True})


@api_view
def sign_up(request):
    """Форма регистрации"""
    registration_form = UserRegistrationRequestForm(request.POST)
    if registration_form.is_valid():
        registration_form.save()
        return Response({'status': True})
    return Response({'message': error_as_dict(registration_form.errors)},
                    status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def sign_in(request):
    """Аутентификация пользователя"""
    if len(request.POST) > 0:
        auth_form = AuthenticationForm(data=request.POST)
    else:
        if request.data != '':
            auth_form = AuthenticationForm(data=request.data)
        else:
            auth_form = AuthenticationForm(data=request.POST)
    if auth_form.is_valid():
        user = auth_form.get_user()
        login(request, user)
        return Response(user.profile.user_profile_as_dict)
