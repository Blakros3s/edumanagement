from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# Define view functions that render template for Staff
@login_required(login_url='/login/')
def staff_page(request):
    return render(request, 'staff/dashboard.html')
