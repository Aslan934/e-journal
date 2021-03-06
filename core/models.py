from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class TeacherManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create new superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class Subject(models.Model):
    name = models.CharField(max_length=200)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class GroupOfStudents(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    students = models.ManyToManyField(Student)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Groups Of Students'


class Teacher(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject, blank=True)
    groupOfStudents = models.ManyToManyField(GroupOfStudents)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


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
