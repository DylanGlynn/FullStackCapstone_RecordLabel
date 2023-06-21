from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.validators import ValidationError
from tzadik_api.serializers import UserSerializer
from tzadik_api.models import ModifiedUser


class ProfileView(ViewSet):
    def list(self, request):
        ''' Docstring. '''
        try:
            serializer = UserSerializer(ModifiedUser.objects.get(user_id=request.auth.user.id))
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    @action(methods=["PUT"], detail=False)
    def edit(self, request):
        ''' Edit the current user's profile. '''

        try:
            updated_user = ModifiedUser.objects.get(user_id=request.auth.user.id)
            updated_user.user.username=request.data['username']
            updated_user.user.password=request.data['password']
            updated_user.user.first_name=request.data['first_name']
            updated_user.user.email=request.data['email_address']
            updated_user.user.last_name=request.data['last_name']
            updated_user. user.is_staff=request.data['is_staff']
            updated_user.is_artist=request.data['is_artist']
            updated_user.is_vendor=request.data['is_vendor']
            updated_user.address_street=request.data['address_street']
            updated_user.address_city=request.data['address_city']
            updated_user.address_state=request.data['address_state']
            updated_user.address_zipcode=request.data['address_zipcode']
            updated_user.payment_type=request.data['payment_type']
            updated_user.save()
            if request.data.get('password', None):
                updated_user.user.set_password(request.data['password'])
            updated_user.save()
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except ModifiedUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
