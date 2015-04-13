"""View declarations"""
from django.template import RequestContext
from django.shortcuts import render_to_response

# Render the main web app views
def index(request):
    """Home view"""
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)

def events(request):
    """Events view"""
    context = RequestContext(request)
    return render_to_response('events.html', {}, context_instance=context)

def about(request):
    """About view"""
    context = RequestContext(request)
    return render_to_response('about.html', {}, context_instance=context)

def signup(request):
    """Sign up view"""
    context = RequestContext(request)
    return render_to_response('signup.html', {}, context_instance=context)

def login(request):
    """Log in view"""
    context = RequestContext(request)
    return render_to_response('login.html', {}, context_instance=context)

def logout(request):
    """Log out view"""
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)

