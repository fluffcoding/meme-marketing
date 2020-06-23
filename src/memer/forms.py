from django import forms

from .models import MemeImages


class MemeSubmissionForm(forms.Form):
    image = forms.ImageField(help_text='Submit your meme here! Maximum size is 2 MB.')