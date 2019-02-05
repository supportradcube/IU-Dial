import uuid
from django.db import models
from languages.fields import LanguageField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils  import timezone

class MyUserManager(BaseUserManager):
    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    """docstring for MyUser"""
    email = models.EmailField(max_length=40, unique=True)
    is_superuser = models.BooleanField(
        'Super User', default=False
    )
    is_staff = models.BooleanField(
        'Staff User', default=False
    )
    is_active = models.BooleanField(
        'Active', default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        """
        :return: the email
        """
        return self.email

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "User Management"


# ----------------------------- Student Module ------------------------------


class Student(models.Model):
    
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False
    )
    username = models.CharField(max_length=40)
    uid = models.CharField(
        max_length=20, null=True, blank=True
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
                                              
    campus_of_enrollment = models.CharField(max_length=100)
    STUDENT_TYPE = (
        ("Graduate", "Graduate"),
        ("Certification", "Certification")
    )
    student_type = models.CharField(
        max_length=13, choices=STUDENT_TYPE
    )
    dc_partner = models.CharField(
        max_length=100
    )
    currently_enrolled = models.BooleanField(default=False)
    pending_enrollment = models.BooleanField(default=False)
    student_name = models.CharField(max_length=40)
    pending_course_request_date = models.DateField()
    course_choice = models.CharField(max_length=50)
    second_course_choice = models.CharField(max_length=50)
    credit_hours_earned = models.PositiveIntegerField()
    campus_affilation = models.CharField(
        max_length=100
    )
    date_of_birth = models.DateField()
    citizenship = models.CharField(max_length=40)
    gender = models.CharField(
        max_length=6
    )
    gender_identity = models.CharField(
        max_length=100
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
    email = models.EmailField(
        max_length=40
    )

    # former names

    former_name = models.BooleanField(default=False)

    former_name_1 = models.CharField(
        max_length=40, null=True, blank=True
    )
    former_name_2 = models.CharField(
        max_length=40, null=True, blank=True
    )
    former_name_3 = models.CharField(
        max_length=40, null=True, blank=True
    )
    former_name_4 = models.CharField(
        max_length=40, null=True, blank=True
    )
    former_name_5 = models.CharField(
        max_length=40, null=True, blank=True
    )

    def __str__(self):
        """
        :return: the id
        """
        return str(self.id)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student"


class Address(models.Model):

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name="student_address"
    )
                        
    # current address
                         
    address = models.TextField()
    city = models.CharField(
        max_length=40
    )
    state = models.CharField(
        "State/Province/Region", max_length=40
    )
    postal_code = models.CharField(
        max_length=12
    )
    country = models.CharField(
        max_length=40
    )
    residency_in_indiana = models.CharField(max_length=40)
    is_permanent_mailing_address = models.BooleanField(
        default=False
    )

    # permanent address

    permanent_address = models.TextField()
    permanent_city = models.CharField(
        max_length=40
    )
    permanent_state = models.CharField(
        "State/Province/Region", max_length=150)
    permanent_postal_code = models.CharField(
        max_length=6
    )
    permanent_country = models.CharField(
        max_length=40
    )

    def __str__(self):
        """
        :return: the student
        """
        return str(self.student)


class EducatorRole(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="role"
    )
    role = models.TextField()

    def __str__(self):
        return str(self.role)


class InstituteAffilation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="affilation"
    )
    institute = models.CharField(max_length=100)
    
    def __str__(self):
         return str(self.institute)


class IUEducationDetails(models.Model):

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="iu_education_details")

    qualtrics_application_id = models.CharField(max_length=40)
    qualtrics_completion_date = models.DateField()
    requested_start_date = models.DateField()
    dc_partner = models.CharField(max_length=100,default='')
    currently_enrolled = models.BooleanField(default=False)
    required_teaching_experience = models.BooleanField(default=False)
    highest_degree = models.CharField(max_length=100)
    state_licensure = models.BooleanField(default=False)
    previous_classwork = models.BooleanField(default=False)
    previous_name = models.CharField(max_length=80)
    educator_role = models.ManyToManyField(
        EducatorRole, related_name="educator_role",default=""
    )
    institution_affilation = models.ManyToManyField(
        InstituteAffilation, related_name="institution_affolation"
    )

    def __str__(self):
        """
        :return: the student
        """
        return str(self.previous_name)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Education Details"



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

    def __str__(self):
        return str(self.response_id)

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
        Qualtrics, on_delete=models.CASCADE,
        related_name="student_details"
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
    
    def __str__(self):
        return str(self.first_name)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student Details"


class IUStudentDetails(models.Model):

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

    def __str__(self):
        return str(self.first_name)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Student IU Details"


class FormerName(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE,
        related_name="former_name"
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
    def __str__(self):
         """Returns the strings"""
         return str(self.Qualtrics)




class Comments(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE,
    verbose_name= "student_comment")
    comment = models.CharField(max_length=255)
    username = models.CharField(max_length=80)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
    
        return self.username

    class Meta:
        verbose_name_plural = "Comments"





# # ---------------------- Grant Enrollemt Data -------------------------------


# class GrantEnrollmentData(models.Model):

#     class_number = models.PositiveIntegerField()
#     course_subject_code = models.CharField(max_length=10)
#     university_id = models.CharField(max_length=10)
#     academic_term_code = models.CharField(max_length=4)
#     grant_id = models.PositiveIntegerField()
    
#     def __str__(self):
#         return str(self.course_subject_code)
    
#     class Meta:
#         verbose_name_plural = 'Grant Enrollment Datasssss'

# # ---------------------------- Grant Data -----------------------------------


class Campus(models.Model):

    campus_id = models.CharField(max_length=10)
    campus = models.CharField(max_length=10)
    grant_name = models.CharField(max_length=10)
    account = models.CharField(max_length=10)
    amount_total = models.FloatField()

    def __str__(self):
        """return campus fields"""
        return str(self.campus)
    
    class Meta:
        verbose_name_plural = 'campus'


class Course(models.Model):

    # grant_en_data = models.ForeignKey(
    #     GrantEnrollmentData, on_delete=models.CASCADE,
    #     related_name="course_detail"
    # )
    course_number = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=5)
    course_desc = models.CharField(max_length=255)
    course_subject_code = models.CharField(max_length=10)
    course_catlog_number = models.PositiveIntegerField()    
    course_official_grade_code = models.CharField(max_length=4) 
    term = models.CharField(max_length=100)
    campus_instrucation = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    total_seats = models.PositiveIntegerField()
    enroll = models.CharField(max_length=100)
    pending_enrollment = models.CharField(max_length=20)
    calculated_remaining = models.CharField(max_length=100)
    no_of_drop = models.CharField(max_length=100)
    no_of_withdrawals = models.CharField(max_length=100)
    campus = models.CharField(max_length=100)
    class_number = models.CharField(max_length=100)
    total_seats = models.PositiveIntegerField()
    student_name = models.CharField(max_length=20)
    sectioin = models.CharField(max_length=20)
    course_status = models.CharField(max_length=20)


    def __str__(self):
        return str(self.student_name)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "course"         

# class Instructor(models.Model):

#     grant_en_data = models.ForeignKey(
#         GrantEnrollmentData, on_delete=models.CASCADE,
#         related_name="instructor_detail"
#     )
#     class_inst_name = models.CharField(max_length=80)
#     class_inst_gds_email = models.EmailField(max_length=255)




# # ------------------------- Enrollemt Data ----------------------------------


class EnrollmentData(models.Model):

    # grant_en_data = models.ForeignKey(
    #     GrantEnrollmentData, on_delete=models.CASCADE,
    #     related_name="enrollment_grant"
    # )
    # course_details = models.ForeignKey(
    #     Course, on_delete=models.CASCADE,
    #     related_name="enrollment_course_detail"
    # )
    # instructor_details = models.ForeignKey(
    #     Instructor, on_delete=models.CASCADE,
    #     related_name="enrollment_instructor_detail"
    # )
    student_enrollment = models.ForeignKey(
        Student, on_delete=models.CASCADE,
    )
    # course_enroll = models.ForeignKey(
    #     Course, on_delete=models.CASCADE,
    # )
    firt_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course_number = models.CharField(max_length=20)
    class_number = models.CharField(max_length=20)
    campus_of_enrollment = models.CharField(max_length=20)
    term = models.CharField(max_length=255)
    grant = models.CharField(max_length=255)
    uid = models.CharField(
        max_length=20, null=True, blank=True
    )
    course = models.CharField(max_length=200,default=False)
    class_student = models.CharField(max_length=200,default=False)
    student_funding = models.CharField(max_length=200,default=False)
    student_enrollment = models.CharField(max_length=200,default=False)
    student_grade = models.CharField(max_length=100,default=False)
    credit_house = models.PositiveIntegerField(default=False)
    
    def __str__(self):
        return str(self.first_name)

    class Meta:
     """return EnrollField fields"""
    verbose_name_plural = 'Enrollment Data'

#---------------------------student enrollment histery data-------------------------------#

class StudentEnrollmentHistery(models.Model):
    st_en_data = models.ForeignKey(Student, on_delete=models.CASCADE,
    related_name='student_enrollment_history'
    )
    course = models.CharField(max_length=200)
    class_student = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    student_funding = models.CharField(max_length=200)
    student_enrollment = models.CharField(max_length=200)
    student_grade = models.CharField(max_length=100,null=True)
    credit_house = models.PositiveIntegerField()

    def __str__(self):
        return str(self.course)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = 'Student Enrollment Histery'


#-----------------------------------------------Enrollment--------------------------------------------#

class Enrollment(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE,
    verbose_name= "student_enrollment")

    TERMS = (
        ("One","One"),
        ("Two","Two"),
        ("Three","Three")
    )
    term = models.CharField(max_length=100,choices=TERMS)
    COURSE = (
        ("B.tech","B.tech"),
        ("MBA","MBA"),
        ("BBA","BBA"),
        ("BA","BA")
    )
    course = models.CharField(max_length=100,choices=COURSE)
    FUNDING = (
       ("One","One"),
        ("Two","Two"),
        ("Three","Three") 
    )
    funding = models.CharField(max_length=100, choices=FUNDING)
    date_created = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        """return the username"""
        return str(self.username)

    class Meta:
        """docstring for Meta"""
        verbose_name_plural = "Enrollment Add/Delete"
    



# class LegalDetails(models.Model):
#     qualtrics_detail = models.ForeignKey(
#         Qualtrics, on_delete=models.CASCADE,
#         related_name="legal_details")
#     full_name = models.CharField(max_length=80)
#     formal_disciplinary_action = models.BooleanField(default=False)
#     legal_charges = models.BooleanField(default=False)
#     pending_criminal_charges = models.BooleanField(default=False)
#     restraining_order = models.BooleanField(
#         "Injury to Person/Property", default=False)
#     response = models.CharField(max_length=255)


class OtherDetails(models.Model):
    qualtrics_detail = models.ForeignKey(
        Qualtrics, on_delete=models.CASCADE,
        related_name="other_details")
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


class OthersInfoData(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name= 'student_data'
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
    date_field = models.DateField(default="")  
    educational_benefits = models.BooleanField(default=False)
    formal_disciplinary_action = models.BooleanField(default=False)
    legal_charges = models.BooleanField(default=False)
    state_Licensure = models.BooleanField(default=False)
    currently_enroll = models.BooleanField(default=False)
    previous_classwork = models.BooleanField(default=False)
    pending_criminal_charges = models.BooleanField(default=False)
    restraining_order = models.BooleanField(
        "Injury to Person/Property", default=False
    )         

    def __str__(self):
        return str(self.veteran_family_member)

    class Meta:
        verbose_name_plural = 'Others information Data'


# # ------------------------- Application Data --------------------------------


# class Application(models.Model):

#     qualtrics_detail = models.ForeignKey(
#         Qualtrics, on_delete=models.CASCADE,
#         related_name="student_application"
#     )
#     grant_en_data = models.ForeignKey(
#         GrantEnrollmentData, on_delete=models.CASCADE,
#         related_name="application_university"
#     )
#     application_number = models.CharField(max_length=10)
#     row_effective_date = models.DateField()
#     academic_plan_code = models.CharField(max_length=15)
#     academic_program_code = models.CharField(max_length=15)
#     network_id = models.CharField(max_length=15)
#     campus_email = models.EmailField(
#         max_length=255, null=True, blank=True
#     )
#     other_email = models.EmailField(
#         max_length=255, null=True, blank=True
#     )


#--------------------------------------CurrentAddress-------------------------------------------#


    # qualtrics_detail = models.ForeignKey(
    #     Qualtrics, on_delete=models.CASCADE,
    #     related_name="current_address")
    # address = models.TextField()
    # city = models.CharField(
    #     max_length=40
    # )
    # state = models.CharField(
    #     "State/Province/Region", max_length=150
    # )
    # postal_code = models.CharField(
    #     max_length=6
    # )
    # country = models.CharField(
    #     max_length=40
    # )
    # residency_in_indiana = models.CharField(max_length=50)
    # is_permanent_mailing_address = models.BooleanField(
    #     default=False
    # )
    # def __str__(self):
    #     return str(self.city)

    # class Meta:
    #     """docstring for meta"""
    #     verbose_name_plural = "Current Address"

#-----------------------------------------------------PermanentAddress---------------------------------------#

# class PermanentAddress(models.Model):

#     qualtrics_detail = models.ForeignKey(
#         Qualtrics, on_delete=models.CASCADE,
#         related_name="permanent_address"
#     )
#     address = models.TextField()
#     city = models.CharField(
#         max_length=40
#     )
#     state = models.CharField(
#         "State/Province/Region", max_length=150)
#     postal_code = models.CharField(
#         max_length=6
#     )
#     country = models.CharField(
#         max_length=40
#     )

#     class Meta:
#         """docstring for meta"""
#         verbose_name_plural = "Permanent Address"

