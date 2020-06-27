from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def not_authorized(request):
    return render(request, 'not_authorized.html', {})

"""@login_required
def index(request):
    if request.user.groups.filter(name='business').exists():
        return redirect('/business/campaigns')
    if request.user.groups.filter(name='memer').exists():
        return redirect('/memer/active-campaigns')
    else:
        return redirect('/choose-group')"""