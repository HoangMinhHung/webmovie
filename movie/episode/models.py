from django.db import models

# Create your models here.
from user.models import MovieUser
from film.models import Movie

class Episode(models.Model):
    name = models.CharField(max_length=100)
    episode_url = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.title} - {self.name}'


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
