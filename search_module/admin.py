from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group
admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['email', 'is_superuser', 'Action']

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

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/student/{}/change/'>View/Edit</a>".format(obj.id))


admin.site.register(Student, StudentAdmin)

#------------------------------------------course--------------------------------------------#

class CourseAdmin(admin.ModelAdmin):
        list_display_links = None
        list_display = ['course_subject_code','Action']
        
        def Action(self, obj):
            return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/course/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(Course,CourseAdmin)
#-----------------------------------------------GrantEnrollmentData--------------------------#

class GrantEnrollmentDataAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['class_number']
   
admin.site.register(GrantEnrollmentData,CourseAdmin) 

#-----------------------------------------------IUEducationDetails-----------------------------------------#

class IUEducationDetailsAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display= ['qualtrics_application_id']

admin.site.register(IUEducationDetails)


# class  EducatorRoleAdmin(admin.ModelAdmin):
#    admin.site.register(EducatorRole,EducatorRoleAdmin)

#-------------------------------------------------others information----------------------------------------#

class OtherInformationAdmin(admin.ModelAdmin):
    link_display_link = None
    link_display = ['veteran_member','Action']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/otherinformation/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(OtherInformation, OtherInformationAdmin)

#------------------------------------------------comments--------------------------------------------------#

class CommentsAdmin(admin.ModelAdmin):
    admin.site.register(Comments)

#------------------------------------------------qualtrics--------------------------------------------------#

class QualtricsAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display =['response_id','Action']
    
    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white; ' href='/admin/search_module/qualtrics/{}/change/'>View/Edit</a>".format(obj.id))

admin.site.register(Qualtrics,QualtricsAdmin)

#---------------------------------------------------recipient Details--------------------------------------#

class RecipientDetailsAdmin(admin.ModelAdmin):
    admin.site.register(RecipientDetails)

#--------------------------------------------------Student details-----------------------------------------#

class StudentDetailsAdmin(StudentDetails):
    link_display =['first_name','Action']
admin.site.register(StudentDetails)


#----------------------------------------------------campus------------------------------------------------#
class CampusAdmin(admin.ModelAdmin):
    list_display_links = None
    link_display = ['campus','Action']

    def Action(self, obj):
        return mark_safe("<a class='button btn' style='color:white;' href='admin/search_module/campus/{}/change/'>View/Edit</a>".format(obj.id))
    
admin.site.register(Campus,CampusAdmin)