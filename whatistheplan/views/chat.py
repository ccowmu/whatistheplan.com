"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def chat(request):
    """Chat view"""
    context = RequestContext(request)
    return render_to_response('chat.html', {}, context_instance=context)
