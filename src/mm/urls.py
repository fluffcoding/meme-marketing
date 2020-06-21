from django.contrib import admin
from django.urls import path, include

from .views import not_authorized

urlpatterns = [
    path('admin/', admin.site.urls),
    path('not-authorized/', not_authorized),
    path('accounts/', include('allauth.urls')),
    path('business/', include('business.urls')),
    path('memers/', include('memer.urls')),
]
