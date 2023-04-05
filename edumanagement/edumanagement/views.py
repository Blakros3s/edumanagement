from django.shortcuts import render, redirect

# Create your views here.
def master_layout(request):
    return render(request,'layouts/master.html')