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
]
