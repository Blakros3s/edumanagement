from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from authentication.models import User
from django.contrib import messages
from app_hod.models import *
# Create your views here.

# Define view functions that render template for Student
@login_required(login_url='/login/')
def student_page(request):
    return render(request, 'student/dashboard.html')


# View function to display the user's profile page
@login_required(login_url='/login/')
def profile_page(request):
    # Get the user object for the logged in user
    user = User.objects.get(id = request.user.id)
    context = {
        'user': user
     }
    return render(request, 'student/profile.html', context)


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
        return redirect('studentprofile')
    # If the request method is not POST, redirect to the profile page
    return redirect('studentprofile')


@login_required(login_url='/login/')
def student_notification(request):
    # Filtering out the Student instance of the logged in user
    user = Student.objects.filter(user__user= request.user.id)
    # Retrieving notifications for the student, ordered by created_at in descending order
    for i in user:
        student_id = i.id
        notification = StudentNotification.objects.filter(student=student_id).order_by('-created_at')
        context = {
            'notification': notification
        }
        return render(request, 'student/notification.html', context)
