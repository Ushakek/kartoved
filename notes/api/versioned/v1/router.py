from django.urls import include, path

from core.service import VersionDefaultRouter
from notes import views

router = VersionDefaultRouter()
router.register('', views.NotesViewSet, basename='notes')
