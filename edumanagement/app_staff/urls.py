from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home/', views.staff_page, name="staffpage"),
    path('profile/', views.profile_page, name="staffprofile"),
    path('profile/update/', views.profile_update, name="staffprofile-update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)