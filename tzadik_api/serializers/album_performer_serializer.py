from rest_framework import serializers
from tzadik_api.models import AlbumPerformer


class AlbumPerformerSerializer(serializers.ModelSerializer):
    ''' JSON serializer for performers on albums. '''

    class Meta:
        model = AlbumPerformer
        fields = ('id', 'album', 'performer', 'performer_instrument', )
        depth = 1
