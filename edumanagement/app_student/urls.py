from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home/', views.student_page, name="studentpage"),
    path('profile/', views.profile_page, name="studentprofile"),
    path('profile/update/', views.profile_update, name="studentprofile-update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)