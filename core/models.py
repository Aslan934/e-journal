from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    credits = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    students = models.ForeignKey(
        Student, on_delete=models.CASCADE, default='Student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField()

    def __str__(self):
        return self.subject.name + ' ' + str(self.date)
