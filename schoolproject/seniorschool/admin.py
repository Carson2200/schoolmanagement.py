from django.contrib import admin
from .models import Stream, Teacher, Subject, Student

# Register your models here.


admin.site.register(Stream)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)
