
from django.urls import path

from . import views

app_name = 'school_v1'

urlpatterns = [
    path('school-view/', views.SchoolViewSet.as_view({'get': 'list', 'post': 'create'}), name='school'),
    path('school-view-total/', views.SchoolTotalViewSet.as_view({'get': 'list', }), name='school-total'),
]
