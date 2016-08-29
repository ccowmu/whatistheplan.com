"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render

def about(request):
    """About view"""
    return render(request, 'about.html', {})
