
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from index!")

def events(request):
    return HttpResponse("Hello from events!")

def about(request):
    return HttpResponse("Hello from about!")

def signup(request):
    return HttpResponse("Hello from signup!")

def login(request):
    return HttpResponse("Hello from login!")

def logout(request):
    return HttpResponse("Hello from logout!")

