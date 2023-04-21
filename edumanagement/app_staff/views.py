from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from authentication.models import User
from django.contrib import messages
from app_hod.models import *
# Create your views here.

# Define view functions that render template for Staff
@login_required(login_url='/login/')
def staff_page(request):
    return render(request, 'staff/dashboard.html')


# View function to display the user's profile page
@login_required(login_url='/login/')
def profile_page(request):
    # Get the user object for the logged in user
    user = User.objects.get(id = request.user.id)
    context = {
        'user': user
     }
    return render(request, 'staff/profile.html', context)


# View function to handle profile updates
def profile_update(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Get the user object to be updated
        user = User.objects.get(id = request.POST.get('id'))
        # Update the user's first name, last name, and email fields from the form data
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if a new password was set
        if password is not None and password.strip() != "":
            # Set the user's password to the new password and update the user's session authentication hash
            user.set_password(password)
            update_session_auth_hash(request, user)
        # Save the updated user object
        user.save()
        # Display a success message and redirect to the profile page
        messages.success(request, "Profile Updated Successfully")
        return redirect('staffprofile')
    # If the request method is not POST, redirect to the profile page
    return redirect('staffprofile')


# View function to show notifications for staff users
@login_required(login_url='/login/')
def staff_notification(request):
    # Query the staff user who is currently logged in
    user = Staff.objects.filter(user__user= request.user.id)
    # Loop through the staff users and get their notification history
    for i in user:
        staff_id = i.id
        notification = StaffNotification.objects.filter(staff=staff_id).order_by('-created_at')
        context = {
            'notification': notification
        }
        return render(request, 'staff/notification.html', context)

