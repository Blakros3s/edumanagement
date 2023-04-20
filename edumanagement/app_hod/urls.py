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


]
