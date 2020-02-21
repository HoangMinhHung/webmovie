from django.db import models
from movie.user.models import MovieUser
from movie.director.models import Director
from movie.actor.models import Actor
from movie.category.models import Category
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    movie_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL(), null=True)
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL(), null=True)
    category = models.ForeignKey(Actor, on_delete=models.SET_NULL(), null=True)
    # type =


class Review(models.Model):
    star = models.IntegerField(max_length=1, null=False)
    user = models.ForeignKey(MovieUser, on_delete=models.SET_NULL(), null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE())






