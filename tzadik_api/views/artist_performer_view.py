from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import ArtistPerformer
from tzadik_api.serializers import ArtistPerformerSerializer


class ArtistPerformerView(ViewSet):
    ''' View for performers specific to artists. '''

    def list(self, request):
        ''' GETs a list of Artist performers. '''

        artists_performers = ArtistPerformer.objects.all()
        serializer = ArtistPerformerSerializer(artists_performers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        ''' Handles the GET request for a specific Artist's performers.
        
        Returns:
            Response -- JSON serialized Artist's performers. '''

        try:
            artist_performers = ArtistPerformer.objects.get(pk=pk)
            serializer = ArtistPerformerSerializer(artist_performers)
            return Response(serializer.data)
        except ArtistPerformer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
