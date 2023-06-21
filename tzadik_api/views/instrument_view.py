from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from tzadik_api.models import Instrument
from tzadik_api.serializers import InstrumentSerializer


class InstrumentView(ViewSet):

    def list(self, request):
        ''' Get a list of instruments. '''

        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data)
