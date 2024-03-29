from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
from rest_framework import status
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    renderer_classes,
    schema,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.viewsets import ViewSet

from core.utils import error_as_dict
from users.forms import UserRegistrationRequestForm


@api_view(['GET'])
@ensure_csrf_cookie
def __init__(request):
    return Response({'init': True})


@api_view(['POST'])
@extend_schema(
    parameters=[
        OpenApiParameter('phone', OpenApiTypes.STR, OpenApiParameter.QUERY),
        OpenApiParameter('username', OpenApiTypes.STR, OpenApiParameter.QUERY),
        OpenApiParameter(
            'OpenApiParameter.QUERY', OpenApiTypes.STR, OpenApiParameter.QUERY
        ),
        OpenApiParameter('email', OpenApiTypes.STR, OpenApiParameter.QUERY),
        OpenApiParameter('password1', OpenApiTypes.STR, OpenApiParameter.QUERY),
        OpenApiParameter('password2', OpenApiTypes.STR, OpenApiParameter.QUERY),
    ]
)
def sign_up(request):
    """Форма регистрации"""
    registration_form = UserRegistrationRequestForm(request.data)
    if registration_form.is_valid():
        registration_form.save()
        return Response({'status': True})
    return Response(
        {'message': error_as_dict(registration_form.errors)},
        status.HTTP_400_BAD_REQUEST,
    )


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
        return Response(user.profile.user_profile_json())
    else:
        return Response(
            {'message': error_as_dict(auth_form.errors)}, status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def sign_out(request):
    if request.user.is_authenticated:
        try:
            logout(request)
        except Exception:
            return Response({'sign_out': 'non authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'sign_out': True})
    else:
        return Response({'sign_out': 'non authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
