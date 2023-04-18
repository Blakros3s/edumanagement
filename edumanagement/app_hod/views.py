from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.

# Define view functions that render template for HOD
@login_required(login_url='/login/')
def hod_page(request):
    return render(request, 'hod/dashboard.html')


# View function to display the user's profile page
@login_required(login_url='/login/')
def profile_page(request):
    # Get the user object for the logged in user
    user = User.objects.get(id = request.user.id)
    context = {
        'user': user
     }
    return render(request, 'hod/profile.html', context)


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
        return redirect('hodprofile')
    # If the request method is not POST, redirect to the profile page
    return redirect('hodprofile')



@login_required(login_url='/login/')
def add_student(request):
    courses = Course.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        enrolled_course = request.POST.get('course')
        enrollment_year = request.POST.get('enrollment_year')
        usertype = "student"

        if User.objects.filter(email=email).exists():
            messages.warning(request,"Email is already taken !")
            return redirect('add-student')
        if User.objects.filter(username=username).exists():
            messages.warning(request,"Username is already taken !")
            return redirect('add-student')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            # Create a new UserProfile object 
            profile = UserProfile(user=user, usertype=usertype)
            profile.save()

            course=Course.objects.get(id=enrolled_course)
            
            student = Student(user=profile, student_id=student_id, gender=gender, dob=dob, address=address, phone_number=phone_number, course=course, enrollment_year=enrollment_year)
            student.save()

            messages.success(request,"Student successfully added !")


    context = {
        'course': courses,
     }
    return render(request, 'hod/student_add.html',context)