from django.urls import include, path

from core.service import VersionDefaultRouter
from users import auth

# app_name = 'users'

router = VersionDefaultRouter()
router.path(
    'auth/',
    include(
        [
            path('sign_up/', auth.sign_up, name='sign_up'),
            path('sign_in/', auth.sign_in, name='sign_in'),
            path('sign_out/', auth.sign_out, name='sign_out'),
        ]
    ),
)
