"""view controller for google_signup route"""
from django.template import RequestContext
from django.shortcuts import render

def google_signup(request):
    """Google signup view"""
    context = RequestContext(request)
    return render(request, 'google_signup.html', {})
