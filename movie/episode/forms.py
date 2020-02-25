from django import forms
from .models import Episode, Comment


class EpisodeAddForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['name', 'episode_url', 'movie']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
