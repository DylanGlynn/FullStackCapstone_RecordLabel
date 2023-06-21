from rest_framework import serializers
from tzadik_api.models import PerformerInstrument


class PerformerInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformerInstrument
        fields = ('id', 'performer', 'instrument', 'instrument_name', 'performer_name', )
        depth = 2
