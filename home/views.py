from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

def home(request):
    return render(request, "home.html")

def system_logout(request):
    logout(request)
    return redirect("home")
# Create your views here.
