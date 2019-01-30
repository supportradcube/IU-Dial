from django.shortcuts import render
from django.views import View
from .models import *


class SearchScreenView(View):
    """Landing page / Search screen View"""

    def get(self, request):
        students = Student.objects.all()
        return render(request, 'search_screen.html' ,{'students':students})

# ------------------------ Student Module -----------------------------------

class StudentSearchView(View):
    """Student Search View"""

    def post(self, request):
        students = Student.objects.all()
        if request.POST['first_name']:
            students = students.filter(first_name__icontains=request.POST['first_name'])
        if request.POST['last_name']:
            students = students.filter(last_name__icontains=request.POST['last_name'])
        if request.POST['username']:
            students = students.filter(username__icontains=request.POST['username'])
        if request.POST['enrollment_campus']: 
            students = students.filter(campus_of_enrollment__icontains=request.POST['enrollment_campus'])
        if request.POST['student_type'] != 'Student Type':   
            students = students.filter(student_type__icontains=request.POST['student_type'])
        if request.POST['dc_partner'] != 'Multiselect':
            students =students.filter(dc_partner__icontains=request.POST['dc_partner'])
        if 'currently_enrolled' in request.POST and request.POST['currently_enrolled']:
            students = students.filter(currently_enrolled='True') 

        if 'pending_enrollment' in request.POST and request.POST['pending_enrollment']:
            students = students.filter(pending_enrollment='True') 
        return render(request, 'search_screen.html', {'students': students})
                                 
                                                                                                 
                                         
class StudentDetailsView(View):
    """Student Details View"""

    def get(self, request, student_id):
        student = Student.objects.get(uuid=student_id)
        educationdetails2019 = IUEducationDetails.objects.filter(student=student,requested_start_date__year='2019').first() 
        educationdetails2018 =IUEducationDetails.objects.filter(student=student,requested_start_date__year='2018').first() 
        educationdetails2017 =IUEducationDetails.objects.filter(student=student,requested_start_date__year='2017').first() 
        educationdetails2016 =IUEducationDetails.objects.filter(student=student,requested_start_date__year='2016').first()
        othersdata2019 = OthersInfoData.objects.filter(student=student,date_field__year='2019').first()
        othersdata2018 = OthersInfoData.objects.filter(student=student,date_field__year='2018').first()
        othersdata2017 = OthersInfoData.objects.filter(student=student,date_field__year='2017').first()
        othersdata2016 = OthersInfoData.objects.filter(student=student,date_field__year='2016').first()
        enrollment = StudentEnrollmentHistery.objects.filter(st_en_data=student).first()
        comment = Comments.objects.filter(user=student.id)

        return render(request, 'student_details.html', {'student': student, 'educationdetails2019':educationdetails2019,
        'educationdetails2018':educationdetails2018,'educationdetails2017':educationdetails2017,'educationdetails2016':educationdetails2016, 'enrollment':enrollment,'comment':comment,
        'othersdata2019':othersdata2019,'othersdata2018':othersdata2018,'othersdata2017':othersdata2017,'othersdata2016':othersdata2016})

                                                                                                                                                                                                                  
class UpdateStudentUidView(View):
    """Student Uid Update View"""      
 
    def post(self, request, student_id):
        student = Student.objects.get(uuid=student_id)
        student.uid = request.POST['uid']
        student.save()
        return render(request, 'student_details.html', {'student': student, })
            

# class AddCommentView(View):
#     """Add Comment"""

#     def post(self, request):
#         comment = Comments.objects.get()
#         return render(request, 'student_details.html', {'comment':comment})
        


# ------------------------ Course Module -----------------------------------


class CourseDetailsView(View):
    """Course Details View"""

    def get(self, request):
        return render(request, 'course_details.html')

# ----------------------- Enrollment Module ---------------------------------


class EnrollmentDetailsView(View):
    """Enrollment Details View"""

    def get(self, request):
        return render(request, 'enrollment_details.html')



class AddEnrollmentView(View):
    """ add enrollment view """

    def post(self,request,uuid):
        enrollment = Enrollment.objects.filter(student=student)


        # return redirect("student-details")