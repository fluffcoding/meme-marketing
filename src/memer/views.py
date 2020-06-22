from django.shortcuts import render, get_object_or_404
from mm.decorators import group_required
from business.models import Campaign

from .models import Meme, MemeImages

@group_required('Memer')
def active_campaigns_view(request):
    campaigns = Campaign.objects.filter(running=True)
    context = {
        'campaigns': campaigns,
    }
    return render(request, 'memer/active_campaigns.html', context)


@group_required('Memer')
def post_memes_for_campaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    meme = Meme.objects.filter(campaign=campaign)
    context = {
        'campaign': campaign,
        'meme': meme,
    }
    return render(request, 'memer/post_memes_campaign.html', context)
