from .models import Movie, Review
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "description", "movie_url", "image_url", "director", "category", "type")


class RatingForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=['user', 'star', 'movie']
