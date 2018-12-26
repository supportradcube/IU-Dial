# Student Module

from django.db import models


class StudentDetails(models.Model):

    # Qualtrics

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    response_type = models.CharField(max_length=14)
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
        max_length=80, null=True, blank=True
    )
    latitude = models.DecimalField(
        decimal_places=8, max_digits=20, blank=True, null=True
    )
    longitude = models.DecimalField(
        decimal_places=8, max_digits=20, blank=True, null=True
    )
    distribution = models.CharField(
        max_length=9
    )
    user_language = models.CharField(max_length=5)

    # For IU

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    role = models.CharField(max_length=255)
    affilation = models.CharField(
        max_length=100, null=True, blank=True
    )
    high_school = models.CharField(
        max_length=100, null=True, blank=True
    )
    application_for = models.CharField(
        "What would you like to do?", max_length=50, null=True, blank=True)
    session = models.CharField(
        "When would you like to start?", max_length=20, null=True, blank=True)
    former_student = models.CharField(max_length=3)
    currently_enrolled = models.CharField(max_length=3)

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
        "two-years or more of teaching in the subject area of the coursework to be studied?", max_length=3
    )
    graduate_degree = models.CharField(max_length=100)
    first_spring_course_request = models.CharField(max_length=255)
    second_spring_course_request = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True)
    graduate_certificate_program = models.CharField(max_length=3)
    graduate_program_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    citizenship = models.CharField(max_length=40)

    # Veteran Member?

    veteran_member = models.CharField(max_length=3)
    veteran_family_member = models.CharField(max_length=40)
    educational_benefits = models.CharField(max_length=3)

    # Current Address

    address = models.TextField(blank=True, null=True)
    city = models.CharField(
        max_length=40, blank=True, null=True
    )
    state = models.CharField(
        max_length=150, null=True, blank=True
    )
    postal_code = models.CharField(
        max_length=12, null=True, blank=True
    )
    country = models.CharField(
        max_length=40, null=True, blank=True
    )
    residency_in_indiana = models.CharField(max_length=50)
    is_permanent_mailing_address = models.CharField(
        max_length=3
    )
    # Permanent Address
    permanent_address = models.TextField(
        blank=True, null=True
    )
    permanent_city = models.CharField(
        max_length=40, blank=True, null=True
    )
    permanent_state = models.CharField(
        max_length=150, null=True, blank=True
    )
    permanent_postal_code = models.CharField(
        max_length=12, null=True, blank=True
    )
    permanent_country = models.CharField(
        max_length=40, null=True, blank=True
    )
    gender = models.CharField(
        max_length=6, null=True, blank=True
    )
    gender_info = models.CharField(
        max_length=255, null=True, blank=True
    )
    former_name = models.CharField(max_length=3)

    # Former Name
    former_name_1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    former_name_2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    former_name_3 = models.CharField(
        max_length=80, null=True, blank=True
    )
    former_name_4 = models.CharField(
        max_length=80, null=True, blank=True
    )
    former_name_5 = models.CharField(
        max_length=80, null=True, blank=True
    )
    formal_disciplinary_action = models.CharField(max_length=3)
    legal_charges = models.CharField(max_length=3)
    pending_criminal_charges = models.CharField(max_length=3)
    restraining_order = models.CharField(max_length=3)
    response = models.CharField(max_length=225)

    source = models.CharField(max_length=225)
    program_type = models.CharField(max_length=225)
    program_id = models.CharField(max_length=225)
    user = models.CharField(max_length=225)

    access_zip = models.CharField(max_length=5)
    access_country = models.CharField(max_length=255)
    access_date = models.DateField()
    access_time = models.TimeField()
    inquiry_type = models.CharField(max_length=10)
    q_r_del = models.CharField(max_length=10)
    audience = models.CharField(max_length=225)
    date = models.DateField()
    mobile_device = models.CharField(max_length=3)
    topics = models.CharField(max_length=10)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student Details"
