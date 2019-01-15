from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import Q


class SearchScreenView(View):
    """Landing page / Search screen View"""

    def get(self, request):
        return render(request, 'search_screen.html')

# ------------------------ Student Module -----------------------------------


class StudentSearchView(View):
    """Student Search View"""

    def post(self, request):
        print(request.POST)
        students=Student.objects.all()
    
        # students = Student.objects.filter(first_name__startswith=request.POST['first_name'])
    
        students = Student.objects.filter(Q(username__startswith=request.POST['username']) | Q(uid__startswith=request.POST['uid']) | Q(
            first_name__startswith=request.POST['first_name']) | Q(last_name__startswith=request.POST['last_name']) | Q(campus_of_enrollment__startswith=request.POST['enrollment_campus']) | Q(student_type__startswith=request.POST['student_type']) | Q(dc_partner__startswith=request.POST['dc_partner']))
        print("Search Results : ", students)
        return render(request, 'search_screen.html', {'students': students })
       
       
# class StudentSearchView(View):
#     def get(request):
#         students = Student.objects.all()
#         search=Student(request.POST)
#         if search.is_valid():
#             if search.cleaned_data["first_name"]:
#                students = Student.filter(first_name__startswith=form.cleaned_data["first_name"])
#             elif search.cleaned_data["last_name"]:
#                students = Student.filter(last_name__startswith=form.cleaned_data["last_name"])
#             elif search.cleaned_data["username"]:
#                students = Student.filter(first_name__startswith=form.cleaned_data["username"])
#         print("Search Results : ", students)  
#         return render(request, 'search_screen.html', {'students': students })



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






