from typing import Iterable

from django.db.models import Count

from .models import School


def get_schools_with_annotated_course_enrollments_count_for_students() -> Iterable[School]:
    qs = School.objects.prefetch_related('students')

    for school in qs:
        school._students = school.students.annotate(course_enrollments_count=Count('course_enrollments'))

    return qs
