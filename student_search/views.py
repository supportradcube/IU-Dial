from django.shortcuts import render
from django.views import View
from .models import *


class Home(View):
    """Landing page view"""

    def get(self, request):
        return render(request, 'index.html')
