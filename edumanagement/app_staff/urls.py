from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.staff_page, name="staffpage"),
    path('profile/', views.profile_page, name="staffprofile"),
    path('profile/update/', views.profile_update, name="staffprofile-update"),
    path('notification/', views.staff_notification, name="staff-notification"),
    path('leave/', views.staff_applyleave, name="staff-applyleave"),
    path('attendance/take', views.take_attendance, name="take-attendance"),
    path('attendance/save', views.save_attendance, name="save-attendance"),
    path('attendance/view', views.view_attendance, name="view-attendance"),
]
