from django.contrib import admin

from django.contrib.auth.models import Group, User
admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_filter = []

    def get_queryset(self, obj=None):
        return User.objects.all().exclude(is_superuser=True)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
