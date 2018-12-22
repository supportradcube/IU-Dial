from django.shortcuts import render
from django.views import View
from .models import *


class StudentSearchView(View):
    """Landing page View"""

    def get(self, request):
        return render(request, 'Student Search.html')


class StudentDetailsView(View):
    """Student Details View"""

    def get(self, request):
        return render(request, 'Student Details.html')
