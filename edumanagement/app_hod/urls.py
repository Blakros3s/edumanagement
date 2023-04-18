from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hod_page, name="hodpage"),
    path('profile/', views.profile_page, name="hodprofile"),
    path('profile/update/', views.profile_update, name="hodprofile-update"),
    path('student/add', views.add_student, name="add-student"),
]
