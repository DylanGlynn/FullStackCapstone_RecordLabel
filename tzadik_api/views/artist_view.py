# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from tzadik_api.models import Artist
from tzadik_api.serializers import ArtistSerializer


class ArtistView(ViewSet):
    ''' Artist view. '''

    def list(self, request):
        ''' Handles GET request for all artists

        Returns:
            Response -- JSON serialized artists.'''

        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        ''' Handles GET requests for a single artist.

        Returns:
            Response -- JSON serialized artist.
        '''

        try:
            artist = Artist.objects.get(pk=pk)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data)
        except Artist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
