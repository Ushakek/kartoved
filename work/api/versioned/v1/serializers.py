from rest_framework import serializers

from notes.api.versioned.v1.serializers import NoteSerializer
from work.models import WorkModel


class ResponseWorkSerializer(serializers.ModelSerializer):
    """Сериализация модели работы"""

    execution = serializers.SerializerMethodField()

    class Meta:
        model = WorkModel
        fields = [
            'name',
            'task',
            'active',
            'type_work',
            'polygon',
            'polyline',
            'executor',
            'execution',
        ]

    @staticmethod
    def get_execution(obj):
        serializer = NoteSerializer(obj.execution, many=True)
        return serializer.data
