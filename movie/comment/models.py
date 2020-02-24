from django.db import models

# Create your models here.
from user.models import MovieUser


class Comment(models.Model):
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(MovieUser, on_delete=models.SET_NULL, null=True)
