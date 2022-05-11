from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import BasicAuthMixin
from work.api.versioned.v1.serializers import ResponseWorkSerializer
from work.models import WorkModel


class WorkViewSet(BasicAuthMixin, ModelViewSet):
    """ViewSet для заметок"""

    serializer_class = ResponseWorkSerializer
    queryset = WorkModel.objects.all()

    def create(self, request, *args, **kwargs):
        return super(WorkViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.filter(executor=request.user.profile)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
