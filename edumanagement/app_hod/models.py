from django.db import models
from authentication.models import UserProfile

# Create your models here.
# Model class to represent course details
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# Model class to represent student details 
class Student(models.Model):
    # Links to a user profile via a OneToOneField
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    # Additional fields for the student model
    student_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    dob = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    enrollment_year = models.CharField(max_length=100, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"

# Model class to represent staff details 
class Staff(models.Model):
    # Links to a user profile via a OneToOneField
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    # Additional fields for the staff model
    staff_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    doj = models.DateField()
    qualification = models.TextField()
    phone_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"