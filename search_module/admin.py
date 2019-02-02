from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group
admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['email', 'is_superuser', 'Action']
    list_filter = ['email', 'is_superuser']

    exclude = (
        'password', 'groups', 'user_permissions',
        'first_name', 'last_name', 'last_login', 'date_joined'
    )

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/myuser/{}/change/'>View/Edit</a>".format(obj.id))

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(MyUser, UserAdmin)

#--------------------------------------------------student---------------------------------------#

class StudentAddressInline(admin.TabularInline):
    model = Address
    max_num = 1
    
class StudentAdmin(admin.ModelAdmin):
    list_display_links = None
    inlines = [StudentAddressInline, ]
    list_display = ['username','Action']
    list_filter = ['username']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/student/{}/change/'>View/Edit</a>".format(obj.id))


admin.site.register(Student, StudentAdmin)

#------------------------------------------course--------------------------------------------#

# class CourseAdmin(admin.ModelAdmin):
#         list_display_links = None
#         list_display = ['course_subject_code','Action']
#         list_filter = ['course_subject_code']
        
#         def Action(self, obj):
#             return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/course/{}/change/'>View/Edit</a>".format(obj.id))

# admin.site.register(Course,CourseAdmin)
#-----------------------------------------------GrantEnrollmentData--------------------------#

# class GrantEnrollmentDataAdmin(admin.ModelAdmin):
#     list_display_links = None
#     list_display = ['class_number']
#     list_filter = ['class_number']
   
# admin.site.register(GrantEnrollmentData,CourseAdmin) 

#-----------------------------------------------IUEducationDetails-----------------------------------------#

class IUEducationDetailsAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display= ['qualtrics_application_id','Student','Action']
    list_filter = ['qualtrics_application_id']
    def Student(self,obj):
        return obj.student.first_name

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/iueducationdetails/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(IUEducationDetails,IUEducationDetailsAdmin)

class EducatorRoleAdmin(admin.ModelAdmin):
    admin.site.register(EducatorRole)

class InstituteAffilationAdmin(admin.ModelAdmin):
    admin.site.register(InstituteAffilation)

#-------------------------------------------------others information----------------------------------------#

class OthersInfoDataAdmin(admin.ModelAdmin):
    link_display_link = None
    link_display = ['veteran_member','Action']
    link_filter = ['veteran_member']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/othersdata/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(OthersInfoData, OthersInfoDataAdmin)

#------------------------------------------------comments--------------------------------------------------#

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
admin.site.register(Comments,CommentsAdmin)

#------------------------------------------------qualtrics--------------------------------------------------#

class QualtricsAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display =['response_id','Action']
    list_filter =['response_id']
    
    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/qualtrics/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(Qualtrics,QualtricsAdmin)

#---------------------------------------------------recipient Details--------------------------------------#

class RecipientDetailsAdmin(admin.ModelAdmin):
    admin.site.register(RecipientDetails)

#--------------------------------------------------Student details-----------------------------------------#

class StudentDetailsAdmin(admin.ModelAdmin):
    list_display_links = None
    link_display =['first_name','Action']
    list_filter =['first_name']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/studentdetails/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(StudentDetails, StudentDetailsAdmin)


#----------------------------------------------------campus------------------------------------------------#
class CampusAdmin(admin.ModelAdmin):
    list_display_links = None
    link_display = ['campus','Action']
    link_filter = ['campus']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white;' href='admin/search_module/campus/{}/change/'>View/Edit</a>".format(obj.id))
    
admin.site.register(Campus,CampusAdmin)

#----------------------------------------------Student IU Details--------------------------------------------#
class IUStudentDetailsAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['first_name','Action']
    list_filter = ['first_name']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/iustudentdetails/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(IUStudentDetails,IUStudentDetailsAdmin)

#------------------------------------------------CurrentAddress-----------------------------------------#

# class CurrentAddressAdmin(admin.ModelAdmin):
#     list_display_links = None
#     list_display = ['city','Action']

#     def Action(self, obj):
#         return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/currentaddress/{}/change/'>View/Edit</a>".format(obj.id))

# admin.site.register(CurrentAddress, CurrentAddressAdmin)

#-------------------------------------------------PermanentAddress--------------------------------------#

# class PermanentAddressAdmin(admin.ModelAdmin):
#     list_display_links = None
#     list_display = ['city','Action']

#     def Action(self, obj):
#         return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/permanentaddress/{}/change/'>View/Edit</a>".format(obj.id))

# admin.site.register(PermanentAddress, PermanentAddressAdmin)

#----------------------------------------------Instructor------------------------------------------------#

class EnrollmentDataAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['first_name']

admin.site.register(EnrollmentData)

#-----------------------------------------------Instructor--------------------------------------------#
# class InstructorAdmin(admin.ModelAdmin):
#     list_display_links = None
#     list_display = ['class_inst_name','Action']

#     def Action(self, obj):
#          return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/permanentaddress/{}/change/'>View/Edit</a>".format(obj.id))

# admin.site.register(Instructor, InstructorAdmin)


#-----------------------------StudentEnrollmentHistery------------------------------------------------3

class StudentEnrollmentHisteryAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['course','student_enrollment','Action']
    list_filter = ['course','student_enrollment']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/studentenrollmenthistery/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(StudentEnrollmentHistery, StudentEnrollmentHisteryAdmin)

admin.site.register(Enrollment)