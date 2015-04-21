from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    """Log out view"""
    logout(request)
    return HttpResponseRedirect('/')

