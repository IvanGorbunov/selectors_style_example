from rest_framework import serializers

from school.models import School, Student


class TotalStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            'name',
        )


class SchoolTotalSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    students = TotalStudentSerializer(many=True)
    course_enrollments_count = serializers.IntegerField()
    # Note: You need to make sure `course_enrollments_count` is annotated before using this serializer,
    # otherwise it'll throw an exception for missing field.
    # That's why we recommend the usage of `inline_serializer`.

    class Meta:
        model = School
        fields = (
            'name',
            'course_enrollments_count',
            'students',
        )
