"""
Database model for events
Every event is played by many teams
Each event is a specific game
"""
from django.db import models

class Event(models.Model):
    """
    event_name -> MW2 1v1 quickscoping
    game -> Modern Warfare 2
    registered_teams -> many to many
    """
    event_name = models.CharField(max_length=256)
    game = models.ForeignKey('Game')
    date = models.DateTimeField()
    registered_teams = models.ManyToManyField('Team')
