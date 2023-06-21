from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import PerformerInstrument
from tzadik_api.serializers import PerformerInstrumentSerializer


class PerformerInstrumentView(ViewSet):

    def list(self, request):
        ''' GETs a list of performers. '''

        performers = PerformerInstrument.objects.all()
        serializer = PerformerInstrumentSerializer(performers, many=True)
        return Response(serializer.data)
