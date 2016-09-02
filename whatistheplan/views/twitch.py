"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render

def twitch(request):
    """Twitch view"""
    return render(request, 'twitch.html', {})
