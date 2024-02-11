from django.db.models import Count, F
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from school.models import School
from school.selectors import get_schools_with_annotated_course_enrollments_count_for_students
from school.serializers.serializers_spectacular import SchoolSpectacularSerializer
from school.serializers.serializers_spectacular_total import SchoolTotalSpectacularSerializer
from school.serializers.serializers_v1 import SchoolSerializer
from school.serializers.serializers_v1_total import SchoolTotalSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    authentication_classes = []
    permission_classes = []


class SchoolTotalViewSet(ModelViewSet):
    queryset = School.objects.prefetch_related('courses').prefetch_related('courses__student_enrollments').annotate(course_enrollments_count=Count('courses__student_enrollments')).all()
    serializer_class = SchoolTotalSerializer
    authentication_classes = []
    permission_classes = []


class SchoolSpectacularViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSpectacularSerializer
    authentication_classes = []
    permission_classes = []


class SchoolTotalSpectacularViewSet(ModelViewSet):
    queryset = get_schools_with_annotated_course_enrollments_count_for_students() #School.objects.all()
    serializer_class = SchoolTotalSpectacularSerializer
    authentication_classes = []
    permission_classes = []
