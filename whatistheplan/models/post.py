"""Database model for blog posts.
Every post has a user profile associated with it. The author will be displayed as an IRC name.
"""
from django.db import models

class Post(models.Model):
    """
    user -> (UserProfile object)
    title -> Welcome to PLAN!
    date_posted -> 2015-4-28
    html -> <p>test paragraph</p>
    """
    user = models.ForeignKey('UserProfile')
    title = models.TextField(max_length=256)
    date_posted = models.DateTimeField()
    html = models.TextField()
