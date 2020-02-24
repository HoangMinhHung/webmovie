from django import forms
from .models import Episode
from film.models import Movie

class EpisodeAddForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['name', 'link',]
