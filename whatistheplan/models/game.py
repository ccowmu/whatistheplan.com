"""Database model Game"""
from django.db import models

class Game(models.Model):
    """
    game_name -> Counter Strike Source
    """
    game_name = models.CharField(max_length=256)
