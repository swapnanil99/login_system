from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .serializers import RegisterSerializer  

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            context = {"error": "Invalid username or password."}
            return render(request, "accounts/index.html", context)

    return render(request, "accounts/index.html")

def register_view(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Account created successfully!")
            return redirect("login_page")
        return render(
            request,
            "accounts/register.html",
            {"errors": serializer.errors},
        )

    return render(request, "accounts/register.html")


@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login_page")
