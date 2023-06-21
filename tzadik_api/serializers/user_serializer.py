''' User serializer. '''
from rest_framework import serializers
#from django.contrib.auth.models import User
from tzadik_api.models import ModifiedUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModifiedUser
        fields = ('id', 'is_artist', 'is_vendor', 'address_street', 'user',
                  'address_city', 'address_state', 'address_zipcode', 'payment_type')
        depth = 1
