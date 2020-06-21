from django.urls import path
from .views import active_campaigns_view

app_name = 'memer'

urlpatterns = [
    path('active-campaigns', active_campaigns_view, name='active-campaigns'),
]