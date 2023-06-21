from rest_framework import serializers
from tzadik_api.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'selection', 'created_on', 'submission_datetime', )
        depth = 2
