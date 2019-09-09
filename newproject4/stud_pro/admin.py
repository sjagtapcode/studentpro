from django.contrib import admin
from stud_pro.models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Teacher_Subject)
admin.site.register(Class)
admin.site.register(Class_Teacher)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Attendance_Marks)
