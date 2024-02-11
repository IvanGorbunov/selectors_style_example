from rest_framework import serializers

from school.models import Course, StudentCourseEnrollment, School


class Course1Serializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Course
        fields = (
            'name',
        )


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    course = Course1Serializer()

    class Meta:
        model = StudentCourseEnrollment
        fields = (
            'course',
        )


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    course_enrollments = CourseEnrollmentSerializer(many=True)

    class Meta:
        model = StudentCourseEnrollment
        fields = (
            'name',
            'course_enrollments',
        )


class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    students = StudentSerializer(many=True)

    class Meta:
        model = School
        fields = (
            'name',
            'students',
        )
