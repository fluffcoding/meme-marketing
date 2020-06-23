from django import forms

from .models import MemeImages


class MemeSubmissionForm(forms.Form):
    image = forms.ImageField()