"""view controller for Sponsors route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def sponsors(request):
    """Sponsors view"""
    context = RequestContext(request)
    return render_to_response('sponsors.html', {}, context_instance=context)
