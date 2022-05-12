from rest_framework import serializers

from notes.models import ModelNotes


class NoteSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()

    def create(self, validated_data):
        validated_data['user_profile'] = self.context['request'].user.profile
        note = super(NoteSerializer, self).create(validated_data)
        return note

    class Meta:
        model = ModelNotes
        fields = (
            'id',
            'coordinates',
            'description',
            'photo',
            'user_profile',
        )

    @staticmethod
    def get_user_profile(obj):
        return {obj.user_profile.id: obj.user_profile.phone}
