"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def forum(request):
    """forum view"""
    context = RequestContext(request)
    return render_to_response('forum.html', {}, context_instance=context)
