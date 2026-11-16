from django.shortcuts import render

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