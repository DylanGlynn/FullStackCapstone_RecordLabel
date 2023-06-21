from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import Album, Track
from tzadik_api.serializers import TrackSerializer


class TrackView(ViewSet):
    ''' Tzadik album's tracks view. '''

    def list(self, request):
        ''' GET a list of an album's tracks.'''

        tracks = Track.objects.all()
        album = Album.objects.get()
