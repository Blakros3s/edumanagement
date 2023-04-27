from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import *
from app_hod.models import *
from app_staff.models import *
from app_student.models import *

class CourseList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data":serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        course.delete()
        return Response({"msg": "Data deleted successfully!"},status=status.HTTP_200_OK)
    

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data":serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response({"msg": "Data deleted successfully!"},status=status.HTTP_200_OK)


class StaffList(APIView):
    def get(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffDetail(APIView):
    def get_object(self, id):
        try:
            return Staff.objects.get(id=id)
        except Staff.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        staff = self.get_object(id)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def put(self, request, id):
        staff = self.get_object(id)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        staff = self.get_object(id)
        staff.delete()
        return Response({"msg": "Data deleted successfully!"},status=status.HTTP_200_OK)


class SubjectList(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetail(APIView):
    def get_object(self, id):
        try:
            return Subject.objects.get(id=id)
        except Subject.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        subject = self.get_object(id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, id):
        subject = self.get_object(id)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        subject = self.get_object(id)
        subject.delete()
        return Response({"msg": "Data deleted successfully!"},status=status.HTTP_200_OK)


class StaffNotificationList(APIView):
    def get(self, request):
        notifications = StaffNotification.objects.all()
        serializer = StaffNotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffNotificationDetail(APIView):
    def get_object(self, id):
        try:
            return StaffNotification.objects.get(id=id)
        except StaffNotification.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        notification = self.get_object(id)
        serializer = StaffNotificationSerializer(notification)
        return Response(serializer.data)

    def put(self, request, id):
        notification = self.get_object(id)
        serializer = StaffNotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        notification = self.get_object(id)
        notification.delete()
        return Response({"msg": "Data deleted successfully!"},status=status.HTTP_200_OK)
    

class StudentNotificationList(APIView):
    def get(self, request):
        student_notifications = StudentNotification.objects.all()
        serializer = StudentNotificationSerializer(student_notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentNotificationDetail(APIView):
    def get_object(self, id):
        try:
            return StudentNotification.objects.get(id=id)
        except StudentNotification.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student_notification = self.get_object(id)
        serializer = StudentNotificationSerializer(student_notification)
        return Response(serializer.data)

    def put(self, request, id):
        student_notification = self.get_object(id)
        serializer = StudentNotificationSerializer(student_notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student_notification = self.get_object(id)
        student_notification.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)
    

class StaffLeaveList(APIView):
    def get(self, request):
        staff_leaves = StaffLeave.objects.all()
        serializer = StaffLeaveSerializer(staff_leaves, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffLeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffLeaveDetail(APIView):
    def get_object(self, id):
        try:
            return StaffLeave.objects.get(id=id)
        except StaffLeave.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        staff_leave = self.get_object(id)
        serializer = StaffLeaveSerializer(staff_leave)
        return Response(serializer.data)

    def put(self, request, id):
        staff_leave = self.get_object(id)
        serializer = StaffLeaveSerializer(staff_leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        staff_leave = self.get_object(id)
        staff_leave.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)
    

class AttendanceList(APIView):
    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceDetail(APIView):
    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        attendance = self.get_object(id)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, id):
        attendance = self.get_object(id)
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        attendance = self.get_object(id)
        attendance.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)


class AttendanceReportList(APIView):
    def get(self, request):
        attendance_reports = AttendanceReport.objects.all()
        serializer = AttendanceReportSerializer(attendance_reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceReportDetail(APIView):
    def get_object(self, id):
        try:
            return AttendanceReport.objects.get(id=id)
        except AttendanceReport.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        attendance_report = self.get_object(id)
        serializer = AttendanceReportSerializer(attendance_report)
        return Response(serializer.data)

    def put(self, request, id):
        attendance_report = self.get_object(id)
        serializer = AttendanceReportSerializer(attendance_report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        attendance_report = self.get_object(id)
        attendance_report.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)
    

class StudentResultList(APIView):
    def get(self, request):
        student_results = StudentResult.objects.all()
        serializer = StudentResultSerializer(student_results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentResultDetail(APIView):
    def get_object(self, id):
        try:
            return StudentResult.objects.get(id=id)
        except StudentResult.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student_result = self.get_object(id)
        serializer = StudentResultSerializer(student_result)
        return Response(serializer.data)

    def put(self, request, id):
        student_result = self.get_object(id)
        serializer = StudentResultSerializer(student_result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student_result = self.get_object(id)
        student_result.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)
    

class StudentLeaveList(APIView):
    def get(self, request):
        student_leaves = StudentLeave.objects.all()
        serializer = StudentLeaveSerializer(student_leaves, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentLeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentLeaveDetail(APIView):
    def get_object(self, id):
        try:
            return StudentLeave.objects.get(id=id)
        except StudentLeave.DoesNotExist:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student_leave = self.get_object(id)
        serializer = StudentLeaveSerializer(student_leave)
        return Response(serializer.data)

    def put(self, request, id):
        student_leave = self.get_object(id)
        serializer = StudentLeaveSerializer(student_leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student_leave = self.get_object(id)
        student_leave.delete()
        return Response({"msg": "Data deleted successfully!"}, status=status.HTTP_200_OK)