from django.db import models
from user.models import MovieUser
from director.models import Director
from actor.models import Actor
from category.models import Category
from type.models import Type
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    movie_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)


class Review(models.Model):
    star = models.IntegerField(max_length=1, null=False)
    user = models.ForeignKey(MovieUser, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)






