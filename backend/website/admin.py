from django.contrib import admin
from website.models import CERT, EXP, Project, User

# Register your models here.
for i in [CERT, EXP, Project, User]:
    admin.site.register(i)