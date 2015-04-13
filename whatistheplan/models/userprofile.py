from django.contrib.auth.models import User
from django.db import models

# Example:
# user -> (Django built-in User class)
# name -> Eugene M'TnDew
# email -> le_euphoric_fedora@yahoo.com
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    name = models.CharField(max_length=256, unique=False)
    email = models.CharField(max_length=256, unique=False)
