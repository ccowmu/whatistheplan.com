"""view controller for events route"""
from django.template import RequestContext
from django.shortcuts import render

def events(request):
    """Events view"""
    return render(request, 'events.html', {})
