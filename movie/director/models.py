from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length = 50)
    dob = models.DateField()
    nationality = models.CharField(max_length = 50)