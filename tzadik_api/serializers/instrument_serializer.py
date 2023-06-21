from rest_framework import serializers
from tzadik_api.models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name',)
        depth = 0
