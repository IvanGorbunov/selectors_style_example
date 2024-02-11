from drf_spectacular.utils import inline_serializer
from rest_framework import serializers


class SchoolSpectacularSerializer(serializers.Serializer):
    name = serializers.CharField()
    students = inline_serializer(name='Students', many=True, fields={
        'name': serializers.CharField(),
        'course_enrollments': inline_serializer(name='Course enrollments', many=True, fields={
            'course': inline_serializer(name='Course', fields={
                'name': serializers.CharField(),
            })
        })
    })
