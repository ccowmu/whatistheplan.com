"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render

def forum(request):
    """forum view"""
    context = RequestContext(request)
    return render(request, 'forum.html', {})
