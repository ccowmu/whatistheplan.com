"""view controller for home route"""
from django.template import RequestContext
from django.shortcuts import render

def index(request):
    """Home view"""
    return render(request, 'home.html', {})
