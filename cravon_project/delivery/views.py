from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    #return HttpResponse("Hello from Cravon 🚀")
    # to connect frontend and backend below render is used
    # in one line frontend page is connected
    return render(request, "index.html")

def open_signup(request):
    return render(request, "signup.html")

def open_signin(request):
    return render(request, "signin.html")

def signup(request): #if the entered details are correct or not
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        return HttpResponse(f"Username: {username}, Password: {password}, Email: {email}, Mobile: {mobile}, Address: {address}")
    else:
        return HttpResponse("Invalid response!")