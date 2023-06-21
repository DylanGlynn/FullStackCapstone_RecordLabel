from django.db import models

class AlbumPerformer(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    performer = models.ForeignKey('Performer', on_delete=models.CASCADE)
    performer_instrument = models.ForeignKey('PerformerInstrument', on_delete=models.CASCADE)
