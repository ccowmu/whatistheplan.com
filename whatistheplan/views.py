"""View declarations"""
from whatistheplan.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Render the main web app views
def index(request):
    """Home view"""
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)

def events(request):
    """Events view"""
    context = RequestContext(request)
    return render_to_response('events.html', {}, context_instance=context)

def about(request):
    """About view"""
    context = RequestContext(request)
    return render_to_response('about.html', {}, context_instance=context)

def signup(request):
    """Sign up view"""
    context = RequestContext(request)

    registered = False
    # Check if the user hit POST /signup, not GET /signup
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return render_to_response('login.html',
                {'login_msg': 'account created'},
                context_instance=context)
        else:
            return render_to_response('signup.html',
                {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered,
                'signup_msg': 'creating account',
                'user_errors': user_form.errors,
                'profile_errors': profile_form.errors},
                context_instance=context)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('signup.html',
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
        'signup_msg': 'creating account'},
        context_instance=context)

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

@login_required
def user_logout(request):
    """Log out view"""
    logout(request)
    return HttpResponseRedirect('/home/')

