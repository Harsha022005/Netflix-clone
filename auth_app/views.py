from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm


# Create your views here.
def HomePage(request):
    return render(request, "home.html")


def LoginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        log = authenticate(request, username=username, password=password)
        if log is not None:
            login(request, log)
            print("Authentication successful, redirecting to home...")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            print("Authentication failed, redirecting to home...")
    return render(request, "login.html")


def SignupView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})
