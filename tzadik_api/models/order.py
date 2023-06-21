from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_on = models.DateTimeField(auto_now_add=True)
    submission_datetime = models.DateTimeField(null=True, blank=True)
    selection = models.ManyToManyField('Album', through="OrderedAlbum", related_name="orders")

@property
def total(self):
    ''' Calculate the order total.

    Returns:
        float: The sum of the product prices on the order.
    '''

    return sum([p.price for p in self.selection.all()], 0)

def __str__(self):
    is_open = 'Completed' if self.submission_datetime else 'Open'
    return f'{is_open} order for {self.user.get_full_name()}'

