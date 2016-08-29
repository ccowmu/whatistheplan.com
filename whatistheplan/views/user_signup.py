"""view controller for user signup route"""
from whatistheplan.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

def user_signup(request):
    """Sign up view"""
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
            return HttpResponseRedirect('/login/')

        else:
            return render(
                request,
                'signup.html',
                {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered,
                    'signup_msg': 'creating account',
                    'user_errors': user_form.errors,
                    'profile_errors': profile_form.errors
                }
            )
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(
        request,
        'signup.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered,
            'signup_msg': 'creating account'
        }
    )
