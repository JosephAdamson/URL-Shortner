from xmlrpc.client import Boolean
from django.db import models
from django.forms import CharField, DateTimeField

# Create your models here.

class ShortURL(models.Model):

    original_url = models.URLField(max_length=1000)
    short_url = models.CharField(max_length=100, unique=True)
    has_alias = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url