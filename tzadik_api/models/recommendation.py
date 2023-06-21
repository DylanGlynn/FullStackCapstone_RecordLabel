from django.db import models


class Recommendation(models.Model):
    recommender = models.ForeignKey('Artist', on_delete=models.CASCADE)
    album_recommendation = models.ForeignKey('Album', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
