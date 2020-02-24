from django import forms

from .models import Type


class TypeAddForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["name", "note"]
