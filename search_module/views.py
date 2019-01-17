from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import Q


class SearchScreenView(View):
    """Landing page / Search screen View"""

    def get(self, request):
        students = Student.objects.all()
        return render(request, 'search_screen.html' ,{'students':students})

# ------------------------ Student Module -----------------------------------


class StudentSearchView(View):
    """Student Search View"""

    def post(self, request):
        print(request.POST)
        students = Student.objects.all()
        # import pdb
        # pdb.set_trace()
        students = students.filter(first_name__icontains=request.POST['first_name'])
        students = students.filter(last_name__icontains=request.POST['last_name'])
        students = students.filter(username__icontains=request.POST['username']) 
        students = students.filter(campus_of_enrollment__icontains=request.POST["enrollment_campus"]) 
        students = students.filter(uid__icontains=request.POST['uid'])

        print("Search Results : ", students)
        return render(request, 'search_screen.html', {'students': students})
                                 
        # students = Student.objects.filter(Q(username__contains=request.POST['username']) | Q(uid__search=request.POST['uid']) | Q(
        # first_name__startswith=request.POST['first_name']) | Q(last_name__startswith=request.POST['last_name']) | Q(campus_of_enrollment__contains=request.POST['enrollment_campus']) | Q(student_type__search=request.POST['student_type']) | Q(dc_partner__search=request.POST['dc_partner'])).order_by()
                
                                         
class StudentDetailsView(View):
    """Student Details View"""

    def get(self, request, student_id):
        student = Student.objects.get(uuid=student_id)
        return render(request, 'student_details.html', {'student': student} )


class UpdateStudentUidView(View):
    """Student Uid Update View"""

    def post(self, request, student_id):
        student = Student.objects.get(uuid=student_id)
        student.uid = request.POST['uid']
        student.save()
        return render(request, 'student_details.html', {'student': student, })


class AddCommentView(View):
    """Add Comment"""

    def post(self, request):
        print(request.POST)
        pass


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
