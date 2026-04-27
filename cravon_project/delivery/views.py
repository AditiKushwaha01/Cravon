from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    #return HttpResponse("Hello from Cravon 🚀")
    # to connect frontend and backend below render is used
    # in one line frontend page is connected
    return render(request, "index.html")