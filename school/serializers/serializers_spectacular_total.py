from drf_spectacular.utils import inline_serializer
from rest_framework import serializers


class SchoolTotalSpectacularSerializer(serializers.Serializer):
    name = serializers.CharField()
    students = inline_serializer(name='Students total', source='_students', many=True, fields={
        # ______________________________________________^
        'name': serializers.CharField(),
        'course_enrollments_count': serializers.IntegerField()  # We now have this annotated!
    })
