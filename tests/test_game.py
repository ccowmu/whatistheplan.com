from django.test import Client, TestCase
from whatistheplan.models import Game

class GameTest(TestCase):
    def setUp(self):
        self.g1 = Game.objects.create(game_name='Counter Strike Source')

    def test_game_name(self):
        """Game has a name"""
        self.assertEqual(self.g1.game_name, 'Counter Strike Source')

    def tearDown(self):
        self.g1.delete()
