"""Forms for use in whatistheplan"""
#pylint: disable=no-init, old-style-class, too-few-public-methods
from whatistheplan.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    """Form for user signup"""
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: #pylint: disable=missing-docstring
        model = User
        fields = (
            'username',
            'password',
            'email'
        )

class UserProfileForm(forms.ModelForm):
    """Form for user profile"""
    class Meta: #pylint: disable=missing-docstring
        model = UserProfile
        fields = (
            'name',
            'irc',
            'steamid',
            'mac_address'
        )
