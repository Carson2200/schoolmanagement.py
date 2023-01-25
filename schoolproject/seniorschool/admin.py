from django.contrib import admin
from .models import Stream, Teacher, Subject, Student

# Register your models here.

class StreamTable(admin.ModelAdmin):
    list_display = ('Stream_Name', 'Stream_Name')

admin.site.register(Stream, StreamTable)

class Teachertabe(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'profile_pic', 'Stream','Subject')
admin.site.register(Teacher, Teachertabe)


class SubjectTable(admin.ModelAdmin):
    list_display = ('Subject_Code','Subject_Name')

admin.site.register(Subject, SubjectTable)



class StudentTable(admin.ModelAdmin):
    list_display = ('Admission_no','first_name','last_name','dob','Parent_phone_number',
                'profile_pic','age','location', 'date_entered','last_updated','Stream' )

admin.site.register(Student, StudentTable)
