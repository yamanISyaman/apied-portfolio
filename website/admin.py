from django.contrib import admin
from website.models import CERT, EXP, Project

# Register your models here.
for i in [CERT, EXP, Project]:
    admin.site.register(i)