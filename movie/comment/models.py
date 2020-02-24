from django.db import models

# Create your models here.
from user.models import MovieUser


class Comment(models.Model):
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(MovieUser, on_delete=models.SET_NULL, null=True)
    episode =

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"Comment {self.content} by {self.user.name}"
