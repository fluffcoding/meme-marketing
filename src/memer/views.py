from django.shortcuts import render
from mm.decorators import group_required
from business.models import Campaign

@group_required('Memer')
def active_campaigns_view(request):
    campaigns = Campaign.objects.filter(running=True)
    context = {
        'campaigns': campaigns,
    }
    return render(request, 'memer/active_campaigns.html', context)