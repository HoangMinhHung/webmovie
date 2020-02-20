from django import forms
from django.contrib.auth.models import User
from .models import MovieUser, Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = MovieUser
        fields = ['username', 'email', 'password1', 'password2']
