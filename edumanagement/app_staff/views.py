from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from authentication.models import User
from django.contrib import messages
from app_hod.models import *
from . models import *
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

# staff applies for leave and the leave data is saved
def staff_applyleave(request):
    # get all leave instances for the current user
    leave = StaffLeave.objects.filter(staff__user__user=request.user.id)
    context = {
        'data': leave
    }
    if request.method == "POST":
        date= request.POST.get('date')
        message = request.POST.get('message')
        staff = Staff.objects.get(user__user=request.user.id)

        leave= StaffLeave(staff=staff, data=date, message=message)
        leave.save()
        messages.success(request, "Applied for Leave Successfully")
        return redirect('staff-applyleave')
    return render(request, 'staff/leave.html',context)


# staff takes attendance for a selected subject and date
def take_attendance(request):
    # get the current user's staff instance
    staff = Staff.objects.get(user__user = request.user.id)
    # get all subjects associated with the staff instance
    subject = Subject.objects.filter(staff=staff)
    action = request.GET.get('action')
    get_student = None
    get_subject = None
    date = None
    if action is not None:
        # get the selected subject and date from the POST request
        sub_id = request.POST.get('subject')
        date = request.POST.get('date')
        get_subject = Subject.objects.get(id = sub_id)

        sub = Subject.objects.filter(id=sub_id)
        # initialize a variable to store all students associated with the selected subject
        for i in sub:
            student_id = i.course.id
            get_student = Student.objects.filter(course_id=student_id)
    context = {
        'staff':staff, 'subject':subject, 'get_subject':get_subject, 'get_date':date, 'students':get_student, 'action':action
    }
    return render(request, 'staff/take_attendance.html',context)


def save_attendance(request):
    # Get the subject id and date of attendance from POST request
    sub_id = request.POST.get('sub')
    date = request.POST.get('date')
    # Get the subject object using the subject id
    get_subject = Subject.objects.get(id = sub_id)
    # Get a list of student ids from POST request
    student_id= request.POST.getlist('attendance')
    # Create a new attendance instance with the subject and attendance date
    attendance = Attendance(subject=get_subject, attendance_data=date)
    attendance.save()

    # Loop through the list of student ids
    for i in student_id:
        std_id = int(i)

        present_students = Student.objects.get(id=std_id)
        # Create a new attendance report instance for the student and attendance
        attendance_report = AttendanceReport(student=present_students,attendance=attendance)
        attendance_report.save()
    
    messages.success(request, "Attendance Saved Successfully")
    return redirect('take-attendance')


# staff views attendance for a selected subject and date
def view_attendance(request):
    staff = Staff.objects.get(user__user = request.user.id)
    subject = Subject.objects.filter(staff=staff)
    action = request.GET.get('action')
    get_report = None
    get_subject = None
    date = None
    if action is not None:
        sub_id = request.POST.get('subject')
        date = request.POST.get('date')
        get_subject = Subject.objects.get(id = sub_id)

        attendance= Attendance.objects.filter(subject=get_subject, attendance_data=date)
        for i in attendance:
            attendance_id = i.id
            get_report = AttendanceReport.objects.filter(attendance_id=attendance_id)
    context = {
        'staff':staff, 'subject':subject, 'get_subject':get_subject, 'get_date':date, 'attendance_report':get_report, 'action':action
    }
    return render(request, 'staff/view_attendance.html',context)