from rest_framework import serializers
from django.contrib.auth.models import User
from tzadik_api.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('id', 'recommender', 'album_recommendation', )
        depth = 1
