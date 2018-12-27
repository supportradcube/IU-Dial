from django.db import models
from languages.fields import LanguageField

# --------------------------- Qualtrics Database ---------------------------


class Qualtrics(models.Model):

    ip_address = models.GenericIPAddressField()
    progress = models.PositiveIntegerField()
    RESPONSE_TYPE = (
        ("IP Address", "IP Address"),
        ("Survey Preview", "Survey Preview")
    )
    response_type = models.CharField(max_length=14, choices=RESPONSE_TYPE)
    response_id = models.CharField("Application ID", max_length=30)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    finished = models.BooleanField(default=False)
    recorded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Qualtrics Data"


class RecipientDetails(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="recipient_details")

    recipient_first_name = models.CharField(
        max_length=40, null=True, blank=True,
    )
    recipient_last_name = models.CharField(
        max_length=40, null=True, blank=True
    )
    recipient_email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    external_data_reference = models.CharField(
        max_length=80, null=True, blank=True
    )
    latitude = models.DecimalField(
        decimal_places=8, max_digits=15, blank=True, null=True
    )
    longitude = models.DecimalField(
        decimal_places=8, max_digits=15, blank=True, null=True
    )
    DISTRIBUTION = (
        ("anonymous", "anonymous"),
        ("preview", "preview")
    )
    distribution = models.CharField(
        max_length=9, choices=DISTRIBUTION
    )

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Recipient Details"


class StudentDetails(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="student_details")
    UID = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=20
    )
    CONTACT_METHOD = (
        ("Text", "Text"),
        ("Call", "Call"),
        ("Text,Call", "Text,Call")
    )
    contact_method = models.CharField(
        max_length=10, choices=CONTACT_METHOD
    )
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=6
    )
    gender_info = models.CharField(
        max_length=255
    )
    citizenship = models.CharField(max_length=40)

    role = models.CharField(max_length=255)
    affilated_institution = models.CharField(
        max_length=255
    )
    high_school = models.CharField(
        max_length=255
    )
    APPLICATION = (
        ("take a graduate course", "take a graduate course"),
        ("explore IU Online", "explore IU Online")
    )
    application_for = models.CharField(max_length=50, choices=APPLICATION)
    session = models.CharField(max_length=20)
    former_student = models.BooleanField(default=False)
    currently_enrolled = models.BooleanField(default=False)
    user_language = LanguageField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student Details"


class EducationDetails(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="education_details")
    iu_id = models.CharField(
        max_length=10
    )
    first_name = models.CharField(
        max_length=40
    )
    last_name = models.CharField(
        max_length=40
    )
    graduate_degree = models.CharField(max_length=100)
    first_spring_course_request = models.CharField(max_length=255)
    second_spring_course_request = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    graduate_certificate_program = models.BooleanField(default=False)
    graduate_program_name = models.CharField(max_length=255)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student IU Details"


class CurrentAddress(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="current_address")
    address = models.TextField()
    city = models.CharField(
        max_length=40
    )
    state = models.CharField(
        max_length=150
    )
    postal_code = models.CharField(
        max_length=12
    )
    country = models.CharField(
        max_length=40
    )
    residency_in_indiana = models.CharField(max_length=50)
    is_permanent_mailing_address = models.BooleanField(
        default=False
    )

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Current Address"


class PermanentAddress(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="permanent_address")
    address = models.TextField()
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

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Permanent Address"


class VeteranDetails(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="veteran_details")
    veteran_member = models.BooleanField(default=False)
    veteran_family_member = models.CharField(max_length=40)
    educational_benefits = models.BooleanField(default=False)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Veteran Details"


class FormerName(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="former_name")
    former_name = models.BooleanField(default=False)

    former_name_1 = models.CharField(
        max_length=80
    )
    former_name_2 = models.CharField(
        max_length=80
    )
    former_name_3 = models.CharField(
        max_length=80
    )
    former_name_4 = models.CharField(
        max_length=80
    )
    former_name_5 = models.CharField(
        max_length=80
    )


class LegalDetails(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="legal_details")
    full_name = models.CharField(max_length=80)
    formal_disciplinary_action = models.BooleanField(default=False)
    legal_charges = models.BooleanField(default=False)
    pending_criminal_charges = models.BooleanField(default=False)
    restraining_order = models.BooleanField(default=False)
    response = models.CharField(max_length=255)


class OtherDetails(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="other_details")
    source = models.CharField(max_length=255)
    program_type = models.CharField(max_length=255)
    program_id = models.CharField(max_length=255)
    user = models.CharField(max_length=255)

    access_zip = models.CharField(max_length=5)
    access_country = models.CharField(max_length=255)
    access_date = models.DateField()
    access_time = models.TimeField()
    inquiry_type = models.CharField(max_length=10)
    q_r_del = models.CharField(max_length=10)
    audience = models.CharField(max_length=255)
    date = models.DateField()
    mobile_device = models.BooleanField(default=False)
    topics = models.CharField(max_length=10)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Other Details"


class EnrollmentData(models.Model):

    # Grant Enrollment Data Sheet

    class_number = models.PositiveIntegerField()
    course_subject_code = models.CharField(max_length=10)
    present_university_id = models.CharField(max_length=10)
    academic_term_code = models.PositiveIntegerField()
    grant_id = models.PositiveIntegerField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Enrollment Data"


class Enrollment(models.Model):

    # Enrollment Data

    enrollment_details = models.ForeignKey(
        EnrollmentData, on_delete=models.CASCADE, related_name="enrollment_details")

    # class_number = models.PositiveIntegerField()
    # course_subject_code = models.CharField(max_length=10)
    # present_university_id = models.CharField(max_length=10)
    # academic_term_code = models.PositiveIntegerField()

    institution_code = models.CharField(max_length=5)
    course_official_grade_code = models.CharField(max_length=5)
    enrollment_add_date = models.DateField()
    enrollment_drop_date = models.DateField(null=True, blank=True)
    course_id = models.CharField(max_length=5)
    course_description = models.CharField(max_length=100)
    course_cateloge_number = models.PositiveIntegerField()
    class_instructor_name = models.CharField(max_length=80)
    class_instructor_email = models.EmailField()
    campus_location_code = models.CharField(max_length=2)
    student_without_description = models.CharField(
        max_length=100, null=True, blank=True)
    student_with_description = models.CharField(
        max_length=100, null=True, blank=True)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Enrollment"


class Application(models.Model):

    # Application Data

    university_id = models.CharField(max_length=10)
    application_number = models.CharField(max_length=10)
    row_effective_date = models.DateField()
    academic_plan_code = models.CharField(max_length=15)
    academic_program_code = models.CharField(max_length=15)
    institution_code = models.CharField(max_length=5)
    first_name = models.CharField(
        max_length=40
    )
    last_name = models.CharField(
        max_length=40
    )
    middle_name = models.CharField(
        max_length=40
    )
    other_email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    campus_email = models.EmailField(
        max_length=255, null=True, blank=True
    )
    network_id = models.CharField(max_length=15)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Application"


class ClassData(models.Model):

    # Class Data

    class_number = models.PositiveIntegerField()
    course_id = models.CharField(max_length=5)
    academic_term_code = models.PositiveIntegerField()
    class_instructor_name = models.CharField(max_length=80)
    class_instructor_email = models.EmailField()
    campus = models.CharField(max_length=5)
    enrollment_cap = models.PositiveIntegerField()
    enrollment_total = models.PositiveIntegerField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Class Data"


class University(models.Model):

    # Grant Data

    university_id = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    account = models.CharField(max_length=10)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    campus = models.CharField(max_length=5)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "University"
