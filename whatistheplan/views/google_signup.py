"""view controller for google_signup route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def google_signup(request):
    """Google signup view"""
    context = RequestContext(request)
    return render_to_response('google_signup.html', {}, context_instance=context)
