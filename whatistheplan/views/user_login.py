"""view controller for user login route"""
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def user_login(request):
    """Log in view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
            else:
                return render(
                    request,
                    'login.html',
                    {'login_msg': 'user is inactive, please talk to an admin.'}
                )
        else:
            return render(
                request,
                'login.html',
                {'login_msg': 'invalid credentials!'}
            )
    else:
        return render(
            request,
            'login.html',
            {'login_msg': 'please log in:'}
        )
