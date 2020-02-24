from django.db import models
from film.models import Movie

# Create your models here.
class Episode(models.Model):
    name = models.CharField(max_length=100)
    episode_url = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
