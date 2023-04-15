from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# Define view functions that render template for HOD
@login_required(login_url='/login/')
def hod_page(request):
    return render(request, 'hod//dashboard.html')