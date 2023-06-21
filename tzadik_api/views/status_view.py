from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from tzadik_api.models import Status
from tzadik_api.serializers import StatusSerializer


class StatusView(ViewSet):
    def list(self, request):
        ''' Get a list of statuses. '''

        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)
