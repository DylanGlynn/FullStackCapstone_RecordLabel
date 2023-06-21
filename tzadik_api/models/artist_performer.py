from django.db import models


class ArtistPerformer(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='artistperformer')
    performer = models.ForeignKey('Performer', on_delete=models.CASCADE)
