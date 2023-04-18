from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.student_page, name="studentpage"),
    path('profile/', views.profile_page, name="studentprofile"),
    path('profile/update/', views.profile_update, name="studentprofile-update"),
]