from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    band_name = models.CharField(max_length=255)
    biography = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255)
