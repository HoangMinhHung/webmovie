from .models import Actor
from django import forms


class ActorForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = Actor
        fields = ('name', 'dob', 'nationality')
