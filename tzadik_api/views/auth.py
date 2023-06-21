from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import ModifiedUser
from tzadik_api.serializers import UserSerializer


class UserView(ViewSet):
    def list(self, request):
        ''' Get the current user. '''

        active_user = ModifiedUser.objects.all(user=request.auth.user)
        serializer = UserSerializer(active_user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    ''' Handles the authentication of a user. 
    
    Method arguments:
        Request -- the full HTTP request object.
    '''

    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'staff': authenticated_user.is_staff
        }
        return Response(data)

    data = {'valid': False}
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    ''' Handles the creation of a new user for authentication. 
    
    Method arguments:
        Request -- the full HTTP request object
    '''

    try:
        new_user = User.objects.create(
            username=request.data['username'],
            password=request.data['password'],
            first_name=request.data['first_name'],
            email=request.data['email_address'],
            last_name=request.data['last_name'],
            is_staff=request.data['is_staff']
        )

        modified_user = ModifiedUser.objects.create(
            user=new_user,
            is_artist=request.data['is_artist'],
            is_vendor=request.data['is_vendor'],
            address_street=request.data['address_street'],
            address_city=request.data['address_city'],
            address_state=request.data['address_state'],
            address_zipcode=request.data['address_zipcode'],
            payment_type=request.data['payment_type']
        )

    except IntegrityError:
        return Response({'message': 'An account with that email address already exists.'},
                        status=status.HTTP_400_BAD_REQUEST)

    modified_user.save()

    token = Token.objects.create(user=modified_user.user)
    data = {'token': token.key}
    return Response(data)


@api_view(["PUT"])
@permission_classes([AllowAny])
def update(request):
    ''' Handles the update request for a user. '''

    try:
        updated_user = ModifiedUser.objects.get(user=request.auth.user)
        updated_user.user.username=request.data['username']
        updated_user.user.password=request.data['password']
        updated_user.user.first_name=request.data['first_name']
        updated_user.user.email=request.data['email_address']
        updated_user.user.last_name=request.data['last_name']
        updated_user.user.is_staff=request.data['is_staff']
        updated_user.is_artist=request.data['is_artist']
        updated_user.is_vendor=request.data['is_vendor']
        updated_user.address_street=request.data['address_street']
        updated_user.address_city=request.data['address_city']
        updated_user.address_state=request.data['address_state']
        updated_user.address_zipcode=request.data['address_zipcode']
        updated_user.payment_type=request.data['payment_type']
        updated_user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    except ValidationError as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    except ModifiedUser.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
