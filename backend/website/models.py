from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime


class User(AbstractUser):
    
    full_name = models.CharField(max_length=50)
    about = models.TextField(null=True)
    image = models.ImageField(upload_to="users/", blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True)
    phone = models.CharField(max_length=15, blank=True)
    telegram = models.URLField(blank=True)
    github = models.URLField(blank=True)


class CERT(models.Model):
    title = models.CharField(max_length=100, blank=False)
    details_url = models.URLField(blank=True)
    donor = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to="certs/", blank=True)
    granted_on = models.DateField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certs")


class SKILL(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=50, blank=True)
    image = models.FileField(upload_to="skills/", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")


class EXP(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exps")

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    code_url = models.URLField(null=True, blank=True)
    preview_url = models.URLField(null=True, blank=True)
    created_at = models.DateField(default=datetime.date.today, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
