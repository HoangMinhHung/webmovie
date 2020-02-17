from django.db import models
from django.utils.dateformat import Formatter
from django.utils import dateformat


# Create your models here.


class Actor(models.Model):
    name = models.TextField(max_length=100)
    dob = models.DateField()
    nationality = models.TextField(max_length=50)

    def __str__(self):
        return self.name
