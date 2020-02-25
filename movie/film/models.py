from django.db import models
from director.models import Director
from actor.models import Actor
from category.models import Category
from type.models import Type
from user.models import MovieUser
# Create your models here.
from episode.models import Episode


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    movie_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    star = models.IntegerField(max_length=1, null=False)
    user = models.ForeignKey(MovieUser, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(MovieUser, on_delete=models.SET_NULL, null=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="comments", null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"Comment '{self.content}' by {self.user.username}"

