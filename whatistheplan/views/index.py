"""view controller for home route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    """Home view"""
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)
