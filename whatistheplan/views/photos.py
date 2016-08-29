"""view controller for photos route"""
from django.template import RequestContext
from django.shortcuts import render

def photos(request):
    """Photos view"""
    context = RequestContext(request)
    return render(request, 'photos.html', {})
