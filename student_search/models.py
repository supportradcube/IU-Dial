# from django.db import models


# class StudentDetails(models.Model):

#     # Demographic data

#     UID = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     recipient_email = models.EmailField(
#         max_length=40, unique=True
#     )
#     recipient_first_name = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     recipient_last_name = models.CharField(
#         max_length=40, null=True, blank=True
#     )

#     # Location

#     latitude = models.DecimalField(
#         decimal_places=8, max_digits=12, blank=True, null=True
#     )
#     longitude = models.DecimalField(
#         decimal_places=8, max_digits=12, blank=True, null=True
#     )

#     # General

#     language = models.CharField(max_length=20, null=True, blank=True)

#     legal_first_name = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     legal_last_name = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     educator_role = models.CharField(
#         "Great! We are excited to help you. To see what is available, please tell us a little more about your role as an educator. Select all that apply.", max_length=100, null=True, blank=True
#     )
#     institution = models.CharField(
#         "Which institution(s) are you affiliated with?", max_length=100, null=True, blank=True
#     )
#     purpose = models.CharField(
#         "What would you like to do?", max_length=100, null=True, blank=True)
#     start_session = models.CharField(
#         "When would you like to start?", max_length=100, null=True, blank=True
#     )

#     # IU Student?

#     former_enrollment = models.BooleanField(default=False)
#     currently_enrolled = models.BooleanField(default=False)

#     # if yes

#     iu_id = models.CharField(max_length=40)
#     first_name = models.CharField(
#         max_length=40
#     )
#     last_name = models.CharField(
#         max_length=40
#     )
#     email = models.EmailField(
#         max_length=40, unique=True
#     )
#     confirm_email = models.EmailField(
#         max_length=40, unique=True
#     )
#     phone_number = models.CharField(
#         max_length=20, null=True, blank=True
#     )
#     contact_method = models.CharField(
#         max_length=10, null=True, blank=True
#     )

#     date_of_birth = models.DateField(
#         null=True, blank=True
#     )
#     citizenship = models.CharField(
#         "Which status best describes you?", max_length=40, null=True, blank=True
#     )

#     # Veteran Member?

#     veteran_member = models.BooleanField(default=False)
#     veteran_member = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     benefits = models.BooleanField(default=False)

#     # Current Address

#     address = models.TextField(
#         blank=True, null=True
#     )
#     city = models.CharField(
#         max_length=40, blank=True, null=True
#     )
#     state = models.CharField(
#         max_length=150, null=True, blank=True
#     )
#     postal_code = models.CharField(
#         max_length=12, null=True, blank=True
#     )
#     country = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     is_permanent_address = models.BooleanField(
#         default=False
#     )
#     residency_in_indiana = models.CharField(
#         max_length=40, null=True, blank=True
#     )
#     gender = models.CharField(
#         max_length=6, null=True, blank=True
#     )
#     gender_info = models.CharField(
#         max_length=70, null=True, blank=True
#     )
#     # Former Name

#     former_name = models.CharField(
#         max_length=80, null=True, blank=True
#     )
#     former_name_2 = models.CharField(
#         max_length=80, null=True, blank=True
#     )
#     former_name_3 = models.CharField(
#         max_length=80, null=True, blank=True
#     )
#     former_name_4 = models.CharField(
#         max_length=80, null=True, blank=True
#     )
#     former_name_5 = models.CharField(
#         max_length=80, null=True, blank=True
#     )

#     class Meta:
#         """docstring for meta"""
#         verbose_name_plural = "Student Details"
