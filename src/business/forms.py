from django import forms
from .models import Campaign


class CampaignForm1(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('title','budget')


class CampaignForm2(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('services',)


class CampaignForm3(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('service_type','number_of_memes','description',)