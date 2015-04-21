from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

def user_login(request):
    """Log in view"""
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('login.html',
                    {'login_msg': 'user is inactive, please talk to an admin.'},
                    context_instance=context)
        else:
            return render_to_response('login.html',
                {'login_msg': 'invalid credentials!'},
                context_instance=context)
    else:
        return render_to_response('login.html',
            {'login_msg': 'please log in:'},
            context_instance=context)


