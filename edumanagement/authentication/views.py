from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from .models import UserProfile
from django.contrib import messages
# Create your views here.

# Define the LoginView class which handles the /login endpoint
class LoginView(View):
    # Handles HTTP GET requests
    def get(self, request):
        return render(request,'web/login.html')
    
    # Handles HTTP POST requests
    def post(self, request):
        # Retrieve the username and password submitted in the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using the Django auth module
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # Redirect the user to the appropriate page based on their usertype
            if user.userprofile.usertype == 'hod':
                login(request, user)
                return redirect('hodpage')
            elif user.userprofile.usertype == 'staff':
                login(request, user)
                return redirect('staffpage')
            elif user.userprofile.usertype == 'student':
                login(request, user)
                return redirect('studentpage')
        else:
            messages.success(request, "Invalid login credentials. Please try again.")
        # Redirect the user back to the login page
        return redirect('login')




# Define the RegistrationView class which handles the /register endpoint
class RegistrationView(View):
    def get(self, request):
        return render(request, 'web/register.html')

    def post(self, request):
        # Retrieve the user's registration information submitted in the POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')

        # Create a new User object with the Django User model
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        # Create a new UserProfile object with the usertype field set to the appropriate value
        profile = UserProfile(user=user, usertype=usertype)
        profile.save()
        
        # Redirect the user back to the registration page
        return redirect('register')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You've Successfully Logged Out!")
        return redirect('login')
    
