from django.db import models
from languages.fields import LanguageField

# --------------------------- Qualtrics Database ---------------------------


class Qualtrics(models.Model):

    RESPONSE_TYPE = (
        ("IP Address", "IP Address"),
        ("Survey Preview", "Survey Preview")
    )
    response_type = models.CharField(
        max_length=14, choices=RESPONSE_TYPE, default="IP Address"
    )
    ip_address = models.GenericIPAddressField()
    progress = models.PositiveIntegerField()
    response_id = models.CharField("Application ID", max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.IntegerField()
    finished = models.BooleanField(default=False)
    recorded_date = models.DateTimeField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Qualtrics Data"


class RecipientDetails(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE,
        related_name="recipient_details"
    )
    recipient_first_name = models.CharField(max_length=40)
    recipient_last_name = models.CharField(max_length=40)
    recipient_email = models.EmailField(max_length=255)
    external_data_reference = models.CharField(max_length=80)
    latitude = models.DecimalField(
        decimal_places=8, max_digits=15
    )
    longitude = models.DecimalField(
        decimal_places=8, max_digits=15
    )
    DISTRIBUTION = (
        ("anonymous", "anonymous"),
        ("preview", "preview")
    )
    distribution_channel = models.CharField(
        max_length=9, choices=DISTRIBUTION
    )

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Recipient Details"


class StudentDetails(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="student_details"
    )
    UID = models.CharField(
        max_length=20, null=True, blank=True
    )
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
    gender_identity = models.CharField(
        max_length=255
    )
    citizenship = models.CharField(max_length=40)

    educator_role = models.CharField(max_length=255)
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
    application_for = models.CharField(
        max_length=50, choices=APPLICATION
    )
    session = models.CharField(max_length=20)
    formerly_enrolled = models.BooleanField(default=False)
    currently_enrolled = models.BooleanField(default=False)
    user_language = LanguageField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student Details"


class IUEducationDetails(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="iu_education_details")
    iu_id = models.CharField(
        max_length=10
    )
    first_name = models.CharField(
        max_length=40
    )
    last_name = models.CharField(
        max_length=40
    )
    graduate_degree_holder = models.BooleanField(default=False)
    state_licensure = models.BooleanField(default=False)
    teaching_experience = models.BooleanField(default=False)
    graduate_degree = models.CharField(max_length=255)

    first_course_request = models.CharField(max_length=255)
    second_course_request = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    graduate_certificate_program = models.BooleanField(default=False)
    graduate_certificate_program_name = models.CharField(max_length=255)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student IU Details"


class VeteranDetails(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="veteran_details"
    )
    veteran_member = models.BooleanField(default=False)
    VETERAN_MEMBER = (
        ("No", "No"),
        ("Spouse", "Spouse"),
        ("Parent/Guardian", "Parent/Guardian")
    )
    veteran_family_member = models.CharField(
        max_length=40, choices=VETERAN_MEMBER
    )
    educational_benefits = models.BooleanField(default=False)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Veteran Details"


class CurrentAddress(models.Model):

    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="current_address")
    address = models.TextField()
    city = models.CharField(
        max_length=40
    )
    state = models.CharField(
        "State/Province/Region", max_length=150
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
        Qualtrics, on_delete=models.CASCADE, related_name="permanent_address"
    )
    address = models.TextField()
    city = models.CharField(
        max_length=40
    )
    state = models.CharField(
        "State/Province/Region", max_length=150)
    postal_code = models.CharField(
        max_length=5
    )
    country = models.CharField(
        max_length=40
    )

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Permanent Address"


class FormerName(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="former_name"
    )
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
    restraining_order = models.BooleanField(
        "Injury to Person/Property", default=False)
    response = models.CharField(max_length=255)


class OtherDetails(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE, related_name="other_details")
    source = models.CharField(max_length=255)
    program_type = models.CharField(max_length=255)
    program_id = models.CharField(max_length=255)
    user = models.CharField(max_length=255)

    access_zip = models.CharField(max_length=5)
    access_country = models.CharField(max_length=20)
    access_date = models.DateField()
    access_time = models.TimeField()
    INQUIRY_TYPE = (
        ("Complete", "Complete"),
        ("INP", "INP"),
        ("NOCON", "NOCON")
    )
    inquiry_type = models.CharField(max_length=10, choices=INQUIRY_TYPE)
    q_r_del = models.CharField(max_length=5)
    audience = models.CharField(max_length=255)
    date = models.DateField()
    mobile_device = models.BooleanField(default=False)
    topics = models.CharField(max_length=10)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Other Details"
