from .models import Movie, Comment
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "description", "movie_url", "image_url", "director", "category", "type")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
