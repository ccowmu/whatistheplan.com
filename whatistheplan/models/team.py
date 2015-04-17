"""Database model for teams
Every game played by many teams
Every team has many user profiles
"""
from django.db import models

class Team(models.Model):
    """
    team_name -> The Crows
    game -> (instance of Game class)
    """
    team_name = models.CharField(max_length=256)
    game = models.ForeignKey('Game')
    userprofiles = models.ManyToManyField('UserProfile')
