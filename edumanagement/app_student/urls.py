from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.student_page, name="studentpage"),
    path('profile/', views.profile_page, name="studentprofile"),
    path('profile/update/', views.profile_update, name="studentprofile-update"),
    path('notification/', views.student_notification, name="student-notification"),
    path('leave/', views.student_applyleave, name="student-applyleave"),
    path('attendance/view', views.view_attendance, name="student-attendance"),
]