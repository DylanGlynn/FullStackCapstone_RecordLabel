from rest_framework import serializers
from tzadik_api.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'artist', 'title', 'release_date', 'category',
                  'catalog_number', 'duration', 'price', 'performers',
                  'description', 'artwork_url', 'status', 'series', 'tracks',
                   'album_artist', 'category_name', 'release_status', )
        depth = 1
