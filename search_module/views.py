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
       
        return render(request, 'search_screen.html', {'students': students})
                                 
  
                                         
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
