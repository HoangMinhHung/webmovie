from django.db import models
from actor.models import Actor
from film.models import Movie


# Create your models here.
class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor.name} --- {self.movie.title}"
