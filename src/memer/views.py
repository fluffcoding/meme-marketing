from django.shortcuts import render, get_object_or_404, redirect
from mm.decorators import group_required
from business.models import Campaign

from .models import Meme, MemeImages

from .forms import MemeSubmissionForm

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
    meme_object, created = Meme.objects.get_or_create(campaign=campaign,memer=request.user)
    meme_images = meme_object.memerconnect.all()
    meme_submit_form = MemeSubmissionForm(request.POST or None, request.FILES or None)
    if meme_submit_form.is_valid():
        parent_meme, created = Meme.objects.get_or_create(campaign=campaign,memer=request.user)
        image = meme_submit_form.cleaned_data['image']
        MemeImages.objects.create(parent_meme=parent_meme,image=image)
        return redirect('/')
    context = {
        #'campaign': campaign,
        #'meme': meme_object,
        'meme_images': meme_images,
        'form': meme_submit_form,
    }
    return render(request, 'memer/post_memes_campaign.html', context)



'''
def post_memes_for_campaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    meme_object = Meme.objects.filter(campaign=campaign)
    meme_images = MemeImages.objects.filter(parent_meme=meme_object)
    meme_submit_form = MemeSubmissionForm(request.POST or None, request.FILES or None)
    if meme_submit_form.is_valid():
        parent_meme = get_or_create(campaign=campaign,memer=request.user)
        image = meme_submit_form.cleaned_data['image']
        MemeImages.objects.create(parent_meme=parent_meme,image=image)
        return redirect('/')
    context = {
        'campaign': campaign,
        'meme': meme_object,
        'meme_images': meme_images,
        'form': meme_submit_form,
    }
    return render(request, 'memer/post_memes_campaign.html', context)

    '''