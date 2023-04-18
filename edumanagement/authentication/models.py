from django.db import models
from django.contrib.auth.models import User

# This model represents additional information for the Django User model,
class UserProfile(models.Model):
    # This field establishes a one-to-one relationship with the User model, 
    # where each UserProfile object is linked to a single User object.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Stores the type of user, such as "hod", "staff", or "student".
    usertype = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"