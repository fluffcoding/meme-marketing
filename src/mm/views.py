from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()

def not_authorized(request):
    return render(request, 'not_authorized.html', {})


def index(request):
    return redirect('/accounts/login')


def user_group_specific_redirect(request):
    user_groups = request.user.groups.all()
    
    if user_groups:
        if str(user_groups[0]) == 'Business':
            return redirect('business:my-campaigns')
        elif str(user_groups[0]) == 'Memer':
            return redirect('memer:active-campaigns')
    else:
        return HttpResponse('Choose group')