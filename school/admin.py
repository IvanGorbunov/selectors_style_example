from django.contrib import admin
from django.contrib.admin import ModelAdmin

from school.models import School, Course, Student, StudentCourseEnrollment


@admin.register(School)
class SchoolAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'school',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'school',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )


@admin.register(StudentCourseEnrollment)
class StudentCourseEnrollmentAdmin(ModelAdmin):
    list_display = (
        'id',
        'student',
        'course',
    )
    list_per_page = 25
    list_display_links = (
        'id',
    )
