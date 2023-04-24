from django.db import models
from app_hod.models import *

# Create your models here.
class StaffLeave(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.staff.user.user.first_name} {self.staff.user.user.last_name}"


class Attendance(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject.name
    

class AttendanceReport(models.Model):
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.user.first_name} {self.student.user.user.last_name}"


class StudentResult(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    exam_date = models.DateField()
    assignment_marks = models.IntegerField()
    exam_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.user.first_name} {self.student.user.user.last_name}"
