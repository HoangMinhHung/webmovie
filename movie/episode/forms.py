from django import forms
from .models import Episode

class EpisodeAddForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['name', 'episode_url', 'movie']
