from django.contrib.auth.models import User
from django.db import models

class ModifiedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_artist = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    address_street = models.CharField(max_length=100, blank=True)
    address_city = models.CharField(max_length=100, blank=True)
    address_state = models.CharField(max_length=100, blank=True)
    address_zipcode = models.CharField(max_length=10, blank=True)
    payment_type = models.CharField(max_length=50, blank=True)

    @property
    def full_name(self):
        ''' Complies a full name for a user. '''
        return f'{self.user.first_name} {self.last_name}'
