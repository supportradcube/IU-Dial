# Student Module
from django.db import models


class StudentDetails(models.Model):

    # Qualtrics

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    RESPONSE_TYPE = (
        ("IP Address", "IP Address"),
        ("Survey Preview", "Survey Preview")
    )
    response_type = models.CharField(max_length=14, choices=RESPONSE_TYPE)
    ip_address = models.GenericIPAddressField()
    progress = models.IntegerField()
    duration = models.IntegerField("In Seconds")
    finished = models.BooleanField(default=False)
    recorded_date = models.DateTimeField()
    response_id = models.CharField(max_length=30)
    recipient_last_name = models.CharField(
        max_length=40, null=True, blank=True
    )
    recipient_first_name = models.CharField(
        max_length=40, null=True, blank=True,
    )
    recipient_email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    external_data_reference = models.CharField(
        max_length=80, null=True, blank=True)

    latitude = models.DecimalField(
        decimal_places=8, max_digits=20, blank=True, null=True
    )
    longitude = models.DecimalField(
        decimal_places=8, max_digits=20, blank=True, null=True
    )
    DISTRIBUTION_CHANNEL = (
        ("anonymous", "anonymous"),
        ("preview", "preview")
    )
    distribution = models.CharField(
        max_length=9, choices=DISTRIBUTION_CHANNEL
    )
    user_language = models.CharField(max_length=5)

    # For IU
    first_name = models.CharField(
        max_length=40
    )
    last_name = models.CharField(
        max_length=40
    )
    role = models.CharField(max_length=255)
    affilation = models.CharField(max_length=100, null=True, blank=True)
    high_school = models.CharField(max_length=100, null=True, blank=True)
    application_for = models.CharField(
        "What would you like to do?", max_length=50, null=True, blank=True)
    session = models.CharField(
        "When would you like to start?", max_length=20, null=True, blank=True)
    FORMERLY_ENROLLED = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    former_student = models.CharField(
        max_length=3, choices=FORMERLY_ENROLLED
    )
    CURRENTLY_ENROLLED = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    currently_enrolled = models.CharField(
        max_length=3, choices=CURRENTLY_ENROLLED
    )
    # if formerly enrolled or currently enrolled

    iu_id = models.CharField(
        max_length=10
    )
    iu_first_name = models.CharField(
        max_length=40
    )
    iu_last_name = models.CharField(
        max_length=40
    )
    iu_email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    confirm_iu_email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    contact_method = models.CharField(
        max_length=10, null=True, blank=True
    )
    credentials_submission = models.CharField(max_length=3)
    state_license = models.CharField(max_length=3)
    expertise = models.CharField(
        "Do you have two-years or more of teaching in the subject area of the coursework to be studied?", max_length=3)
    graduate_degree = models.CharField(max_length=100)

    first_spring_course_request = models.CharField(max_length=255)
    second_spring_course_request = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student Details"
