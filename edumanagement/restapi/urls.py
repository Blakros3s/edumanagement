from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:id>/', CourseDetail.as_view(), name='course-detail'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:id>/', StudentDetail.as_view(), name='student-detail'),
    path('staffs/', StaffList.as_view(), name='staff-list'),
    path('staffs/<int:id>/', StaffDetail.as_view(), name='staff-detail'),
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:id>/', SubjectDetail.as_view(), name='subject-detail'),
    path('staff-notifications/', StaffNotificationList.as_view(), name='staffnotification-list'),
    path('staff-notifications/<int:id>/', StaffNotificationDetail.as_view(), name='staffnotification-detail'),
    path('student-notifications/', StudentNotificationList.as_view(), name='studentnotification-list'),
    path('student-notifications/<int:id>/', StudentNotificationDetail.as_view(), name='studentnotification-detail'),
    path('staff-leave/', StaffLeaveList.as_view(), name='staffleave-list'),
    path('staff-leave/<int:id>/', StaffLeaveDetail.as_view(), name='staffleave-detail'),
    path('attendance/', AttendanceList.as_view(), name='attendance-list'),
    path('attendance/<int:id>/', AttendanceDetail.as_view(), name='attendance-detail'),
    path('attendance-report/', AttendanceReportList.as_view(), name='attendancereport-list'),
    path('attendance-report/<int:id>/', AttendanceReportDetail.as_view(), name='attendancereport-detail'),
    path('student-result/', StudentResultList.as_view(), name='studentresult-list'),
    path('student-result/<int:id>/', StudentResultDetail.as_view(), name='studentresult-detail'),
    path('student-leave/', StudentLeaveList.as_view(), name='studentleave-list'),
    path('student-leave/<int:id>/', StudentLeaveDetail.as_view(), name='studentleave-detail'),
    
]