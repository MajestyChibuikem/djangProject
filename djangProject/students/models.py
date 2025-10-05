from django.db import models

# Create your models here.

class students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    surname = models.CharField(null = True)
    course = models.CharField(null = True, max_length=255)


class faculty(models.Model):
    facultyname = models.CharField(max_length = 255)
    facultycourse = models.CharField(max_length = 255)
    facultycolor = models.CharField(null = True,  max_length = 255)

