from django.db import models

# Create your models here.
from django.db import models

from django.db import models

from django.db import models


class Stream(models.Model):
    object = models.manager
    Stream_Name = models.CharField(max_length=40)

    def __str__(self):
        return f'Stream({self.Stream_Name})'


class Student(models.Model):
    # administrator = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    Admission_no = models.CharField(max_length=30, null=True, blank=True, unique=True)
    # gender = models.CharField(max_length=7, null=True, blank=True, choices=gender_category)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    Parent_phone_number = models.CharField(max_length=10, null=True, blank=True)
    profile_pic = models.ImageField(default="Student.jpg", null=True, blank=True)
    age = models.IntegerField(default='0', blank=True, null=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    Stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self, profile_pic=None):
        return f'Student({self.first_name},  {self.last_name}, {profile_pic})'


class Subject(models.Model):
    Subject_Code = models.CharField(max_length=4, null=True, blank=True)
    Subject_Name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'Subject({self.Subject_Code}, {self.Subject_Name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    profile_pic = models.ImageField(default="Student.jpg", null=True, blank=True)
    Stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self, profile_pic=None):
        return f'Teacher({self.first_name}, {self.first_name} {self.profile_pic}'

