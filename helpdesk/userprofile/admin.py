from django.contrib import admin

from userprofile.models import Department, UserProfile


class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)
