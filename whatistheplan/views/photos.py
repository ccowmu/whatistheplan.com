"""view controller for photos route"""
from django.template import RequestContext
from django.shortcuts import render_to_response

def photos(request):
    """Photos view"""
    context = RequestContext(request)
    return render_to_response('photos.html', {}, context_instance=context)
