
"""Student_search app URL Configuration"""

from student_search import views
from django.conf.urls import url
from .views import *

app_name = 'student_search'

urlpatterns = [

    url(r'^$', views.StudentSearchView.as_view(), name='search'),
    url(r'^student-details$', views.StudentDetailsView.as_view(),
        name='student-details'),
    url(r'^course-details$', views.CourseDetailsView.as_view(),
        name='course-details'),
    url(r'^enrollment-details$', views.EnrollmentDetailsView.as_view(),
        name='enrollment-details'),


]
