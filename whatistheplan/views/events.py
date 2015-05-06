"""view controller for events route"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from whatistheplan.models import Event

def events(request, num="1"):
    """Events view, num defaults to 1 if not specified"""
    context = RequestContext(request)

    # How many events to place on a page
    per_page = 5

    return render_to_response('events.html', {}, context_instance=context)
