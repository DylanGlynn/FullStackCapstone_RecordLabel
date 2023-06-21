from rest_framework import serializers
from tzadik_api.models import OrderedAlbum


class OrderSerializer(serializers.ModelSerializer):

    album = serializers.SlugRelatedField(
    many=True,
    read_only=True,
    slug_field="album"
    )

    class Meta:
        model = OrderedAlbum
        fields = ('id', 'album', 'order', )
        depth = 0
