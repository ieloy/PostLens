from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignUpForm

def index(request):
    return render(request, "postlensapp/index.html")

def about(request):
    return render(request, "postlensapp/about.html")

def connect(request):
    return render(request, "postlensapp/connect.html")

def analytics(request):
    return render(request, "postlensapp/analytics.html")

def signin(request):
    return render(request, "postlensapp/signin.html")

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("postlensapp:index")

    else:
        form = SignUpForm()
    return render(request, "postlensapp/register.html", {"form": form})