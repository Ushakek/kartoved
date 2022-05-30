from djeym.models import Polygon, Polyline
from rest_framework import serializers

from notes.api.versioned.v1.serializers import NoteSerializer
from notes.models import ModelNotes
from work.models import WorkModel


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = ['coordinates']


class PolylineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polyline
        fields = ['coordinates']


class ResponseWorkSerializer(serializers.ModelSerializer):
    """Сериализация модели работы"""

    execution = serializers.SerializerMethodField()
    polygon = serializers.SerializerMethodField()
    polyline = serializers.SerializerMethodField()

    class Meta:
        model = WorkModel
        fields = [
            'id',
            'name',
            'task',
            'active',
            'done',
            'type_work',
            'polygon',
            'polyline',
            'executor',
            'execution',
        ]

    @staticmethod
    def get_execution(obj):
        notes = ModelNotes.objects.filter(work=obj)
        serializer = NoteSerializer(notes, many=True)
        return serializer.data

    @staticmethod
    def get_polygon(obj):
        if obj.polygon is not None:
            serializer = PolygonSerializer(obj.polygon)
            return serializer.data
        else:
            return None

    @staticmethod
    def get_polyline(obj):
        if obj.polyline is not None:
            serializer = PolylineSerializer(obj.polyline)
            return serializer.data
        else:
            return None
