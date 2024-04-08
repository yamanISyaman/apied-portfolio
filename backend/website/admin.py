from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from website.models import CERT, EXP, Project, User, SKILL

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'full_name', 'email', 'resume', 'image', 'about', 'phone', 'telegram', 'github', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    


# Register your models here.
admin.site.register(User, UserAdmin)

for i in [CERT, EXP, Project, SKILL]:
    admin.site.register(i)