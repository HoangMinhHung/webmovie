from django.db import models
from django.utils.dateformat import Formatter
from django.utils import dateformat


# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
