from django.db import models


class OrderedAlbum(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
