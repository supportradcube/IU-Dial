from django.shortcuts import render
from django.views import View
from .models import *


class StudentSearchView(View):
    """Landing page / Search screen View"""

    def get(self, request):
        return render(request, 'search_screen.html')


class StudentDetailsView(View):
    """Student Details View"""

    def get(self, request):
        return render(request, 'student_details.html')


class CourseDetailsView(View):
    """Course Details View"""

    def get(self, request):
        return render(request, 'course_details.html')


class EnrollmentDetailsView(View):
    """Enrollment Details View"""

    def get(self, request):
        return render(request, 'enrollment_details.html')


class ErrorPage(View):
    """Error Page View"""

    def get(self, request):
        return render(request, 'error_page.html')