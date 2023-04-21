from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(StaffNotification)
admin.site.register(StudentNotification)
