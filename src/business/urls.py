from django.urls import path
from .views import CreateCampaignView, my_campaign_list, single_campaign
from .forms import CampaignForm1, CampaignForm2, CampaignForm3

app_name= 'business'

urlpatterns = [
    path('create/', CreateCampaignView.as_view([CampaignForm1, CampaignForm2, CampaignForm3]), name='create-campaign'),
    path('campaigns/', my_campaign_list, name='my_campaigns'),
    path('campaign/<id>', single_campaign, name='single-campaign')
]