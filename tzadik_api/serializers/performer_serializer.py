from rest_framework import serializers
from tzadik_api.models import Performer


class PerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        fields = ('id', 'first_name', 'last_name', 'full_name', )
        depth = 1
