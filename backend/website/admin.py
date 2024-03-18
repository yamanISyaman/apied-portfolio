from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from website.models import CERT, EXP, Project, User

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email',  'password')}),
        ('Personal info', {'fields': ('full_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    


# Register your models here.
admin.site.register(User, UserAdmin)

for i in [CERT, EXP, Project]:
    admin.site.register(i)