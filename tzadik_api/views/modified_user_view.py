from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from tzadik_api.models import ModifiedUser
from tzadik_api.serializers import UserSerializer


class ModifiedUserView(ViewSet):

    def list(self, request):
        ''' Get a list of users. '''

        users = ModifiedUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        ''' GET a specific user. '''

        try:
            specific_user = ModifiedUser.objects.get(pk=pk)
            serializer = UserSerializer(specific_user)
            return Response(serializer.data)
        except ModifiedUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
