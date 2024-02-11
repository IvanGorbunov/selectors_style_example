
from django.urls import path

from . import views

app_name = 'school_v2'

urlpatterns = [
    path('school-view/', views.SchoolSpectacularViewSet.as_view({'get': 'list', 'post': 'create'}), name='school'),
    path('school-view-total/', views.SchoolTotalSpectacularViewSet.as_view({'get': 'list', }), name='school-total'),
]
