from django.db import models

# Create your models here.

class students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

