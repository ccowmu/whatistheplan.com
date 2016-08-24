"""view controller for Sponsors route"""
from django.template import RequestContext
from django.shortcuts import render

def sponsors(request):
    """Sponsors view"""
    context = RequestContext(request)
    return render(request, 'sponsors.html', {})
