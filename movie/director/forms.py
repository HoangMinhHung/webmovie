from .models import Director
from django import forms


class DirectorAddForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ["name", "dob", "nationality"]
