from django.contrib import admin
from .models import UserProfile

# Admin configuration for the UserProfile model.
class UserProfileAdmin(admin.ModelAdmin):
    # Displays the user and usertype fields in the admin interface's list view.
    list_display = ('user', 'usertype')

admin.site.register(UserProfile, UserProfileAdmin)

#customizing Admin panel
admin.site.site_title = 'Education Managemnt' # page title
admin.site.site_header = 'Edumanagement' #brand name
admin.site.index_title = 'Admin Panel' # panel name