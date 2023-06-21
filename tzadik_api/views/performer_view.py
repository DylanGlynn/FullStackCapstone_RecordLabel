from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import Performer
from tzadik_api.serializers import PerformerSerializer


class PerformerView(ViewSet):

    def list(self, request):
        ''' GETs a list of performers. '''

        performers = Performer.objects.all()
        serializer = PerformerSerializer(performers, many=True)
        return Response(serializer.data)
