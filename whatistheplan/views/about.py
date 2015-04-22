"""view controller for about route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def about(request):
    """About view"""
    context = RequestContext(request)
    return render_to_response('about.html', {}, context_instance=context)
