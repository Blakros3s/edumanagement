from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StaffLeave)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(StudentResult)