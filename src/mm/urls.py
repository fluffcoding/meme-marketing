from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from django.conf import settings

from .views import not_authorized


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', index),
    path('not-authorized/', not_authorized),
    path('accounts/', include('allauth.urls')),
    path('business/', include('business.urls')),
    path('memers/', include('memer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)