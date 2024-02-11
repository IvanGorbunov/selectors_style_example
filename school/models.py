from django.db import models


class School(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self) -> str:
        return f'School № {self.id}'


class Course(models.Model):
    name = models.CharField(max_length=250)
    school = models.ForeignKey(School, related_name='courses', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self) -> str:
        return f'{self.name}({self.school})'


class Student(models.Model):
    name = models.CharField(max_length=250)
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return f'{self.name}({self.school})'


class StudentCourseEnrollment(models.Model):
    student = models.ForeignKey(Student, related_name='course_enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='student_enrollments', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Student course enrollment'
        verbose_name_plural = 'Student course enrollments'

    def __str__(self) -> str:
        return f'Enrollment: {self.id} - {self.student}({self.course})'
