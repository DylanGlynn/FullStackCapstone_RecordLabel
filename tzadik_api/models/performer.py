from django.db import models


class Performer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):
        ''' Creates the full performer's name. '''
        return f'{first_name} {last_name}'
