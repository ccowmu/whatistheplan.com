from django.template import RequestContext, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)

def events(request):
    context = RequestContext(request)
    return render_to_response('events.html', {}, context_instance=context)

def about(request):
    context = RequestContext(request)
    return render_to_response('about.html', {}, context_instance=context)

def signup(request):
    context = RequestContext(request)
    return render_to_response('signup.html', {}, context_instance=context)

def login(request):
    context = RequestContext(request)
    return render_to_response('login.html', {}, context_instance=context)

def logout(request):
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)

