from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import AlbumPerformer
from tzadik_api.serializers import AlbumPerformerSerializer


class AlbumPerformerView(ViewSet):
    ''' View for performers specific to albums. '''

    def list(self, request):
        ''' GETs a list of album performers. '''

        albums_performers = AlbumPerformer.objects.all()
        serializer = AlbumPerformerSerializer(albums_performers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        ''' Handles the GET request for a specific album's performers.
        
        Returns:
            Response -- JSON serialized album's performers. '''

        try:
            album_performers = AlbumPerformer.objects.get(pk=pk)
            serializer = AlbumPerformerSerializer(album_performers)
            return Response(serializer.data)
        except AlbumPerformer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
