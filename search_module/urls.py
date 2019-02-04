
"""Student_search app URL Configuration"""

from search_module import views
from django.conf.urls import url
from .views import *

app_name = 'search_module'

urlpatterns = [

    url(r'^$', views.SearchScreenView.as_view(), name='search'),

    # Student Module

    url(r'^student-search$', views.StudentSearchView.as_view(), name='student-search'
        ),
    url(r'^student-details/(?P<student_id>[0-9a-f-]+)$', views.StudentDetailsView.as_view(), name='student-details'
        ),
    url(r'^update-uid/(?P<student_id>[0-9a-f-]+)$', views.UpdateStudentUidView.as_view(), name='update-uid'
        ),

    # Course Module

    url(r'^course-details$', views.CourseDetailsView.as_view(),
        name='course-details'),

    # Enrollment Module

    url(r'^enrollment-details$', views.EnrollmentDetailsView.as_view(),
        name='enrollment-details'),
  
    url(r'^add-enrollment/(?P<student_id>[0-9a-f-]+)$', views.AddEnrollmentView.as_view(), name='add-enrollment'),


    url(r'^add-comment/(?P<student_id>[0-9a-f-]+)$', views.AddCommentView.as_view(), name='comment')

    #  url(r'^add-delete/(?P<student_id>[0-9a-f-]+)$', views.DeleteEnrollment.as_view(), name='delete')
    ]
