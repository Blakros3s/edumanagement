from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home/', views.hod_page, name="hodpage"),
    path('profile/', views.profile_page, name="hodprofile"),
    path('profile/update/', views.profile_update, name="hodprofile-update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)