from rest_framework import serializers
from app_hod.models import *
from app_staff.models import *
from app_student.models import *
from authentication.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        exclude = ['created_at', 'updated_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ['created_at', 'updated_at']

class StaffNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffNotification
        exclude = ['created_at']

class StudentNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentNotification
        exclude = ['created_at']

class StaffLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLeave
        exclude = ['created_at']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ['created_at', 'updated_at']

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        exclude = ['created_at', 'updated_at']

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        exclude = ['created_at', 'updated_at']

class StudentLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLeave
        exclude = ['created_at']


