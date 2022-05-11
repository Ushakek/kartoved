from django.urls import include, path

from core.service import VersionDefaultRouter


router = VersionDefaultRouter()
router.path(
    'auth/',
    include(
        [
        ]
    ),
)
