
from django.urls import path, include

urlpatterns = [
    path('school/', include('school.urls_v2')),
]
