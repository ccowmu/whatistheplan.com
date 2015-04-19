"""View declarations"""
from whatistheplan.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response

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
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors()
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('signup.html',
        {'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered},
        context_instance=context)

def login(request):
    """Log in view"""
    context = RequestContext(request)
    return render_to_response('login.html', {}, context_instance=context)

def logout(request):
    """Log out view"""
    context = RequestContext(request)
    return render_to_response('home.html', {}, context_instance=context)

