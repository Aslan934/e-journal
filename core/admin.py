from django.contrib import admin
from core import models
admin.site.register(models.Teacher)
admin.site.register(models.Subject)
admin.site.register(models.Attendance)
admin.site.register(models.Student)
admin.site.register(models.GroupOfStudents)
