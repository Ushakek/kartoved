from rest_framework import serializers

from notes.models import ModelNotes


class NoteSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()

    def create(self, validated_data):
        print(validated_data)
        validated_data['user_profile'] = self.context['request'].user.profile
        note = super(NoteSerializer, self).create(validated_data)
        return note

    class Meta:
        model = ModelNotes
        fields = (
            'coordinates',
            'description',
            'photo',
            'user_profile',
        )
