from django.template import RequestContext
from django.shortcuts import render_to_response

def events(request):
    """Events view"""
    context = RequestContext(request)
    return render_to_response('events.html', {}, context_instance=context)

