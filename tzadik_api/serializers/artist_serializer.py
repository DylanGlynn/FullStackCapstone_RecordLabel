from rest_framework import serializers
from tzadik_api.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    ''' JSON serializer for Artists. '''

    class Meta:
        model = Artist
        fields = ('id', 'band_name', 'biography', 'website_url')
        depth = 1
