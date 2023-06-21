from rest_framework import serializers
from tzadik_api.models import ArtistPerformer

class ArtistPerformerSerializer(serializers.ModelSerializer):
    ''' JSON serializer for performers associated with specific artists. '''

    class Meta:
        model = ArtistPerformer
        fields = ('id', 'artist', 'performer' )
        depth = 2
