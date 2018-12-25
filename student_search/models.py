# Student Module
from django.db import models


class StudentDetail(models.Model):
    """Student Detail Model"""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=80)
