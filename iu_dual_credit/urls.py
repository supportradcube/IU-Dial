
"""iu_dual_credit URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('student_search.urls', namespace='student_search')),
]

