from django.db import models
from app_hod.models import *

# Create your models here.
class StudentLeave(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.user.user.first_name} {self.student.user.user.last_name}"