from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    full_name = models.CharField(max_length=25)
    about = models.TextField(null=True)
    image = models.ImageField(upload_to="users/", blank=True)
    resume = models.FileField(upload_to="resumes", blank=True)
    phone = models.CharField(max_length=15, blank=True)
    telegram = models.URLField(blank=True)
    github = models.URLField(blank=True)


class CERT(models.Model):
    title = models.CharField(max_length=25, blank=False)
    details_url = models.URLField(blank=True)
    donor = models.CharField(max_length=25, blank=True)
    image = models.ImageField(upload_to="certs/", blank=True)
    granted_on = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certs")


class SKILL(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.CharField(max_length=25, blank=True)
    image = models.FileField(upload_to="skills/", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")


class EXP(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exps")

class Project(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=False)
    code_url = models.URLField()
    preview_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
