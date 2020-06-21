from django.shortcuts import render


def not_authorized(request):
    return render(request, 'not_authorized.html', {})