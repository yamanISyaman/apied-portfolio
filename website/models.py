from django.db import models

# Create your models here.
class CERT(models.Model):
    title = models.CharField(max_length=25, blank=False)
    image = models.ImageField(upload_to="certs/", blank=False)
    granted_on = models.DateField()


class EXP(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Project(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to="certs/", blank=False)
    code_url = models.URLField()
    preview_url = models.URLField()
