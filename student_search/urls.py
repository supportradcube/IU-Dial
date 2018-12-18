
"""Student_search app URL Configuration"""

from student_search import views
from django.conf.urls import url
from .views import *

app_name = 'student_search'

urlpatterns = [

    url(r'^$', views.Home.as_view(), name='home'),

]
