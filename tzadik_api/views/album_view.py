# from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import Album, Order
from tzadik_api.serializers import AlbumSerializer


class AlbumView(ViewSet):
    ''' Tzadik album view. '''

    def list(self, request):
        ''' Get a list of albums. '''

        albums = Album.objects.all()
        category = request.query_params.get('category', None)
        if category is not None:
            albums = albums.filter(category=category)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk):
        '''  Handles GET requests for a single album.
        
        Returns:
            Response -- JSON serialized album.
        '''

        try:
            album = Album.objects.get(pk=pk)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)
        except Album.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def create(self, request):
        ''' Create a new album. '''

        try:
            album = Album.objects.create(
                artist=request.data['artistId'],
                title=request.data['title'],
                release_date=request.data['releaseDate'],
                category=request.data['categoryId'],
                catalog_number=request.data['catalogNumber'],
                duration=request.data['duration'],
                price=request.data['price'],
                description=request.data['description'],
                artwork_url=request.data['artworkUrl'],
                status=request.data['statusId'],
                series=request.data['seriesId'],
            )
            serializer = AlbumSerializer(album)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroyer(self, request, pk):
        ''' Delete an album. '''

        try:
            album = Album.objects.get(pk=pk)
            album.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Album.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    @action(methods=["POST"], detail=True)
    def add_to_order(self, request, pk):
        ''' Adding an album to the current user's open order. '''

        try:
            album = Album.objects.get(pk=pk)
            order, _ = Order.objects.get_or_create(
                user=request.auth.user,
                submission_datetime=None,
            )
            order.selection.add(album)
            return Response({'message': 'album added'}, status=status.HTTP_201_CREATED)
        except Album.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    @action(methods=["DELETE"], detail=True)
    def remove_from_order(self, request, pk):
        ''' Removes an album from the current user's open order. '''

        try:
            album = Album.objects.get(pk=pk)
            order = Order.objects.get(
                user=request.auth.user, submission_datetime=None)
            order.selection.remove(album)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except (Album.DoesNotExist, Order.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
