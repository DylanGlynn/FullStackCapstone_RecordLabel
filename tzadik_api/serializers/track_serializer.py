''' Track serializer. '''
from rest_framework import serializers
from tzadik_api.models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'album', 'disc_number', 'track_number', 'track_title', )
