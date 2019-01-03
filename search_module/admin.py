# from django.contrib import admin

# from django.contrib.auth.models import Group, User
# admin.site.unregister(Group)


# class UserAdmin(admin.ModelAdmin):
#     list_filter = []
#     list_display = ['username', 'email', 'is_superuser']
#     # def get_queryset(self, obj=None):
#     #     return User.objects.all().exclude(is_superuser=True)
#     exclude = ('password', 'groups', 'user_permissions',
#                'first_name', 'last_name', 'last_login', 'date_joined')

#     def has_add_permission(self, request):
#         return False


# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
