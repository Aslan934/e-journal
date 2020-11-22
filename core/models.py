from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class TeacherProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Subject(models.Model):
    name = models.CharField(max_length=200)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    subjects = models.ManyToManyField(Subject)


class Student(models.Model):
    name = models.CharField(max_length=250)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject, blank=True)
    groups = models.ManyToManyField(Groups)
    objects = TeacherProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.name


class Attendance(models.Model):
    presence_choices = [('present', 'Present'),
                        ('absent', 'Absent')]
    students = models.ForeignKey(
        Student, on_delete=models.CASCADE, default='Student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    presence = models.CharField(choices=presence_choices, max_length=7)

    def __str__(self):
        return self.subject.name + ' ' + str(self.date)
