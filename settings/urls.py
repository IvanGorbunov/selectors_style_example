
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('settings.urls_api_v1')),
    path('api/v2/', include('settings.urls_api_v2')),

    path('__debug__/', include('debug_toolbar.urls')),
] + doc_url
