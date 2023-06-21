from django.db import models


class Track(models.Model):
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name='tracks')
    disc_number = models.IntegerField()
    track_number = models.IntegerField()
    track_title = models.TextField()
