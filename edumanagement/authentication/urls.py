
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import LoginView, RegistrationView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('hod/', views.hod_page, name="hodpage"),
    path('staff/', views.staff_page, name="staffpage"),
    path('student/', views.student_page, name="studentpage"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
