from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from notes.api.versioned.v1.serializers import NoteSerializer
from notes.models import ModelNotes
from core.permissions import BasicAuthMixin


class NotesViewSet(BasicAuthMixin, ModelViewSet):
    """ViewSet для заметок"""
    serializer_class = NoteSerializer
    queryset = ModelNotes.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user
        print(user)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
