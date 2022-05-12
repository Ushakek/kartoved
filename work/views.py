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
        query_params = self.validate()
        queryset = self.get_queryset()
        queryset = queryset.filter(executor=request.user.profile, active=True)
        if 'done' in query_params:
            queryset = queryset.filter(done=query_params['done'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def validate(self):
        query_params = self.request.query_params
        done = query_params.get('done', None)
        params = {}
        if done is not None:
            if done in ('True', 'true', True):
                params.update({'done': True})
            elif done in ('False', 'false', False):
                params.update({'done': False})

        return params
