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


# View function to add a new student
@login_required(login_url='/login/')
def add_student(request):
    courses = Course.objects.all()
    # Check if the form was submitted
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

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request,"Email is already taken !")
            return redirect('add-student')
        if User.objects.filter(username=username).exists():
            messages.warning(request,"Username is already taken !")
            return redirect('add-student')
        else:
            # Create a new user with the given details
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            # Create a new user profile
            profile = UserProfile(user=user, usertype=usertype)
            profile.save()

            # Get the course object from the provided id
            course=Course.objects.get(id=enrolled_course)

            # Create a new student object with the given details
            student = Student(user=profile, student_id=student_id, gender=gender, dob=dob, address=address, phone_number=phone_number, course=course, enrollment_year=enrollment_year)
            student.save()

            messages.success(request,"Student successfully added !")
            return redirect('add-student')

    context = {
        'course': courses,
     }
    return render(request, 'hod/student_add.html',context)

# View function to list all the students
@login_required(login_url='/login/')
def student_index(request):
    # Query all students from the database
    student = Student.objects.all()
    context = {"data": student}
    return render(request, 'hod/student_index.html', context)

# View function to view student details
@login_required(login_url='/login/')
def student_view(request, id):
    # Query a student from the database based on the id parameter passed in the URL
    student = Student.objects.get(id=id)
    context = {"data": student}
    return render(request, 'hod/student_view.html', context)

# View function to edit student details
@login_required(login_url='/login/')
def student_edit(request, id):
    student = Student.objects.get(id=id)
    courses = Course.objects.all()
    # Format the date of birth of the student object
    dob = student.dob.strftime('%Y-%m-%d')
    context = {"data": student, "course": courses, "dob": dob}
    return render(request, 'hod/student_edit.html', context)

# View function to delete existing student record
@login_required(login_url='/login/')
def student_delete(request, id):
    student = Student.objects.get(id=id)
    # Delete the student object from the database
    student.delete()
    messages.success(request, "Student record deleted successfully")
    return redirect("list-student")

# View function to update student information
def student_update(request):
    # Check if the request method is POST
    if request.method == "POST":
        course = Course.objects.get(id=request.POST.get('course'))
        # Get the user object to be updated
        student = Student.objects.get(id = request.POST.get('id'))
         # Update student's details with the new POST data
        student.user.user.first_name = request.POST.get('first_name')
        student.user.user.last_name = request.POST.get('last_name')
        student.user.user.username = request.POST.get('username')
        student.user.user.email = request.POST.get('email')
        student.student_id = request.POST.get('student_id')
        student.gender = request.POST.get('gender')
        student.dob = request.POST.get('dob')
        student.address = request.POST.get('address')
        student.phone_number = request.POST.get('phone_number')
        student.course = course
        student.enrollment_year = request.POST.get('enrollment_year')
        password = request.POST.get('password')
        # Check if a new password was set
        if password is not None and password.strip() != "":
            # Set the student's password to the new password
            student.user.user.set_password(password)
            print(password)
        
        # Save the updated student and user objects
        student.user.user.save()
        student.save()

        # Redirect the user to the updated student's edit page with a success message
        messages.success(request, "Student Details Updated Successfully")
        return redirect('edit-student',id=student.id)
    # If the request method is not POST, redirect to the edit page with the given student ID
    return redirect('edit-student',id=request.POST.get('id'))

# View function to update user profile details
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

# View function to add a new course
@login_required(login_url='/login/')
def add_course(request):
    # Check if the form was submitted
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        # Check if course name already exists
        if Course.objects.filter(name=course_name).exists():
            messages.warning(request, "Course already exists!")
            return redirect('add-course')
        else:
            # Create a new course with the given course name
            course = Course(name=course_name)
            course.save()

            messages.success(request, "Course successfully added!")
            return redirect('add-course')
    return render(request, 'hod/course_add.html')

# View function to list all courses
@login_required(login_url='/login/')
def course_index(request):
    course = Course.objects.all()
    context = {"data": course}
    return render(request,'hod/course_index.html', context)


# View function to edit course
@login_required(login_url='/login/')
def course_edit(request, id):
    course = Course.objects.get(id=id)
    context = {"data": course}
    return render(request, 'hod/course_edit.html', context)


# View function to delete a course
@login_required(login_url='/login/')
def course_delete(request, id):
    course = Course.objects.get(id=id)
    # Delete the course object from the database
    course.delete()
    messages.success(request, "Course deleted successfully")
    return redirect("list-course")

# View function to update a course
def course_update(request):
    # Check if the form was submitted
    if request.method == "POST":
        course = Course.objects.get(id= request.POST.get('id'))
        course.name = request.POST.get('course_name')

        # Check if course name already exists
        if Course.objects.filter(name=course.name).exists():
            messages.warning(request, "Course already exists!")
            return redirect('edit-course')
        else:
            # Create a new course with the given course name
            course.save()
            messages.success(request, "Course Updated successfully")
            return redirect('edit-course', id=course.id)
    return redirect('edit-course', id= request.POST.get('id'))

