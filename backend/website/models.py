from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    full_name = models.CharField(max_length=25)


class CERT(models.Model):
    title = models.CharField(max_length=25, blank=False)
    image = models.ImageField(upload_to="certs/", blank=True)
    granted_on = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certs")


class EXP(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exps")

class Project(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to="certs/", blank=False)
    code_url = models.URLField()
    preview_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
