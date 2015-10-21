"""Database Model for User Profiles. Each user has one profile"""
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    user -> (Django built-in User class)
    name -> Eugene M'TnDew
    steamid -> dyladan
    """
    user = models.OneToOneField(User, primary_key=True)
    name = models.CharField(max_length=256, unique=False)
    steamid = models.CharField(max_length=256)
    irc = models.CharField(max_length=256, unique=False)
    mac_address = models.CharField(max_length=256, unique=False)
