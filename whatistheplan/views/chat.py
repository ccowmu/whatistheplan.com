"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render

def chat(request):
    """Chat view"""
    return render(request, 'chat.html', {})
