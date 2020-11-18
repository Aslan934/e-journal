from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250, required=True)
    surname = models.CharField(max_length=250, required=True)
    is_present = models.BooleanField()
