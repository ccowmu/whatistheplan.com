"""view controller for user logout route"""

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    """Log out view"""
    logout(request)
    return HttpResponseRedirect('/')
