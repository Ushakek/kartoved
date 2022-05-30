from djeym.models import CategoryPlacemark, Placemark
from rest_framework import serializers

from notes.models import ModelNotes
from work.models import WorkModel


class PlacemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placemark
        fields = ('id', 'header', 'coordinates')


class NoteSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()
    marker = serializers.SerializerMethodField()

    def create(self, validated_data):
        validated_data['user_profile'] = self.context['request'].user.profile
        coordinates = validated_data.get('coordinates')
        work_: WorkModel = validated_data['work']
        ymap = (
            work_.polygon.ymap
            if work_.type_work == WorkModel.POLYGON
            else work_.polyline.ymap
        )
        try:
            placemark: Placemark = Placemark.objects.create(
                ymap=ymap,
                category=CategoryPlacemark.objects.last(),
                header=validated_data.get('name', 'test'),
                body=validated_data.get('description', None),
                icon_slug='mountain',
                coordinates=coordinates,
            )
            placemark.save()
            validated_data['marker'] = placemark
        except Exception:
            pass

        note = super(NoteSerializer, self).create(validated_data)
        return note

    class Meta:
        model = ModelNotes
        fields = (
            'id',
            'name',
            'coordinates',
            'description',
            'photo',
            'user_profile',
            'work',
            'marker',
        )

    @staticmethod
    def get_user_profile(obj: ModelNotes):
        return {obj.user_profile.id: obj.user_profile.phone}

    @staticmethod
    def get_marker(obj: ModelNotes):
        serializer = PlacemarkSerializer(obj.marker)
        return serializer.data
