from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hod_page, name="hodpage"),
    path('profile/', views.profile_page, name="hodprofile"),
    path('profile/update/', views.profile_update, name="hodprofile-update"),

    path('student/add', views.add_student, name="add-student"),
    path('student/', views.student_index, name='list-student'),
    path('student/update/', views.student_update, name='update-student'),
    path('student/view/<int:id>/', views.student_view, name='view-student'),
    path('student/edit/<int:id>/', views.student_edit, name='edit-student'),
    path('student/delete/<int:id>/', views.student_delete, name='delete-student'),

    path('course/', views.course_index, name='list-course'),
    path('course/add', views.add_course, name='add-course'),
    path('course/edit/<int:id>/', views.course_edit, name='edit-course'),
    path('course/delete/<int:id>/', views.course_delete, name='delete-course'),
    path('course/update/', views.course_update, name='update-course'),

    path('staff/add', views.add_staff, name="add-staff"),
    path('staff/', views.staff_index, name='list-staff'),
    path('staff/view/<int:id>/', views.staff_view, name='view-staff'),
    path('staff/edit/<int:id>/', views.staff_edit, name='edit-staff'),
    path('staff/delete/<int:id>/', views.staff_delete, name='delete-staff'),
    path('staff/update/', views.staff_update, name='update-staff'),

    path('subject/add', views.add_subject, name="add-subject"),
    path('subject/', views.subject_index, name="list-subject"),
    path('subject/edit/<int:id>/', views.subject_edit, name='edit-subject'),
    path('subject/delete/<int:id>/', views.subject_delete, name='delete-subject'),
    path('subject/update/', views.subject_update, name='update-subject'),

    path('staff/send_notification', views.send_staffnotification, name='send-staffnotification'),
    path('staff/save_notification', views.save_staffnotification, name='save-staffnotification'),
    path('student/send_notification', views.send_studentnotification, name='send-studentnotification'),
    path('student/save_notification', views.save_studentnotification, name='save-studentnotification'),

    path('staff/leave/', views.staff_leave, name='leave-staff'),
    path('staff/leave/approved/<str:id>', views.staff_approved, name='approved-staff'),
    path('staff/leave/disapproved/<str:id>', views.staff_disapproved, name='disapproved-staff'),
    path('student/leave/', views.student_leave, name='leave-student'),
    path('student/leave/approved/<str:id>', views.student_approved, name='approved-student'),
    path('student/leave/disapproved/<str:id>', views.student_disapproved, name='disapproved-student'),
    
    path('attendance/view', views.view_attendance, name="hod-attendance"),

    path('result/view',views.view_result, name='hod-result'),
    path('result/view/student',views.view_studentresult, name='hod-studentresult')

]
