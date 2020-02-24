from .models import Movie
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "description", "movie_url", "image_url", "director", "category", "type")