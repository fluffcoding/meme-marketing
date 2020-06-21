from django.urls import path
from .views import CreateCampaignView
from .forms import CampaignForm1, CampaignForm2, CampaignForm3

app_name= 'business'

urlpatterns = [
    path('create/', CreateCampaignView.as_view([CampaignForm1, CampaignForm2, CampaignForm3]), name='create-campaign'),
]