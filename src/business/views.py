import os
from django.conf import settings
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .models import Campaign
from django.core.files.storage import FileSystemStorage


class CreateCampaignView(SessionWizardView):
    template_name = 'business/create_campaign.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        a = form_data[0]
        b = form_data[1]
        c = form_data[2]
        final = {**a,**b,**c}
        obj = Campaign(**final)
        obj.user = self.request.user
        obj.save()
        return render(self.request, 'business/done.html',{
            'form_data': [form.cleaned_data for form in form_list],
        })