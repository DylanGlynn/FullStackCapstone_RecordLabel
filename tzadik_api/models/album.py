from django.db import models


class Album(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='albums')
    catalog_number = models.CharField(max_length=10)
    performers = models.ManyToManyField('Performer', related_name="albums")
    duration = models.TextField()
    price = models.FloatField(max_length=4)
    description = models.TextField()
    artwork_url = models.CharField(max_length=255)
    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE, related_name='albums')
    track = models.ManyToManyField("Track", related_name='albums')
    series = models.CharField(max_length=255)

    @property
    def album_artist(self):
        ''' Get album artist name. '''
        return f'{self.artist.band_name}'

    @property
    def category_name(self):
        ''' Get category name for an album. '''
        return f'{self.category.name}'

    @property
    def release_status(self):
        ''' Get release status. '''
        return f'{self.status.name}'