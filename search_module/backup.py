# ------------------------------- Grant Data --------------------------------


class Grant(models.Model):

    grant_id = models.CharField(max_length=10)
    grant_name = models.CharField(max_length=10)
    account = models.CharField(max_length=10)
    amount_total = models.DecimalField(decimal_places=2, max_digits=10)
    campus = models.CharField(max_length=5)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Grant"

# ------------------------- Grant Enrollment Data ---------------------------


class EnrollmentData(models.Model):

    class_number = models.PositiveIntegerField()
    course_subject_code = models.CharField(max_length=10)
    present_university_id = models.CharField(max_length=10)
    academic_term_code = models.PositiveIntegerField()
    grant_id = models.PositiveIntegerField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Enrollment Data"

# ------------------------------- Class Data --------------------------------


class ClassData(models.Model):

    enrollment_details = models.ForeignKey(
        EnrollmentData, on_delete=models.CASCADE, related_name="class_data")
    # class_number = models.PositiveIntegerField()
    # academic_term_code = models.PositiveIntegerField()
    course_id = models.CharField(max_length=5)
    class_instructor_name = models.CharField(max_length=80)
    class_instructor_email = models.EmailField()
    campus = models.CharField(max_length=5)
    enrollment_cap = models.PositiveIntegerField()
    enrollment_total = models.PositiveIntegerField()

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Class Data"

# ---------------------------- Enrollment Data ------------------------------


class Enrollment(models.Model):

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
    course_description = models.CharField(max_length=100)
    course_cateloge_number = models.PositiveIntegerField()

    # course_id = models.CharField(max_length=5)
    # class_instructor_name = models.CharField(max_length=80)
    # class_instructor_email = models.EmailField()

    campus_location_code = models.CharField(max_length=2)
    student_without_description = models.CharField(
        max_length=100, null=True, blank=True)
    student_with_description = models.CharField(
        max_length=100, null=True, blank=True)

    class Meta:
        """docstring for meta"""
        verbose_name_plural = "Enrollment"

# ---------------------------- Application Data -----------------------------


class Application(models.Model):

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
