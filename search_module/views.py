from django.shortcuts import render
from django.views import View
from .models import *


class StudentSearchView(View):
    """Landing page / Search screen View"""

    def get(self, request):
        students = Student.objects.all()
        return render(request, 'search_screen.html', {'students': students, })


class StudentDetailsView(View):
    """Student Details View"""

    def get(self, request, student_id):
        student = Student.objects.get(uuid=student_id)
        return render(request, 'student_details.html', {'student': student, })


class CourseDetailsView(View):
    """Course Details View"""

    def get(self, request):
        return render(request, 'course_details.html')


class EnrollmentDetailsView(View):
    """Enrollment Details View"""

    def get(self, request):
        return render(request, 'enrollment_details.html')
