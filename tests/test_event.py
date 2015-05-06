from django.test import Client, TestCase
from whatistheplan.models import Event, Team, Game, UserProfile
from django.contrib.auth.models import User
from django.utils import timezone

class EventTest(TestCase):
    # Create a game, two users, two teams, and then the event
    def setUp(self):
        self.game = Game.objects.create(game_name='Modern Warfare 2')
        self.game.save()

        self.u1 = User.objects.create_user('username', 'email@email.com', 'password')
        self.u2 = User.objects.create_user('dickweed', 'email2@email.com', 'password')
        self.u1.save()
        self.u2.save()

        self.up1 = UserProfile.objects.create(user=self.u1, name="Lil Jon")
        self.up2 = UserProfile.objects.create(user=self.u2, name="dan", steamid="dyladan")
        self.up1.save()
        self.up2.save()

        self.t1 = Team.objects.create(team_name='The Crows', game=self.game)
        self.t2 = Team.objects.create(team_name='Wildlings', game=self.game)
        self.t1.save()
        self.t2.save()

        self.ev1 = Event.objects.create(
            event_name='Modern Warfare 2 Quickscoping Contest',
            game=self.game,
            date=timezone.now(),
        )
        self.ev1.save()
        self.ev1.registered_teams.add(self.t1)
        self.ev1.registered_teams.add(self.t2)
        self.ev1.save()

    def test_event_name(self):
        self.assertEqual(self.ev1.event_name, 'Modern Warfare 2 Quickscoping Contest')

    def test_event_teams(self):
        self.assertEqual(self.ev1.registered_teams.count(), 2)
        self.assertEqual(self.ev1.registered_teams.filter(team_name='The Crows')[0], self.t1)
        self.assertEqual(self.ev1.registered_teams.filter(team_name='Wildlings')[0], self.t2)

    def tearDown(self):
        self.game.delete()
        self.u1.delete()
        self.u2.delete()
        self.up1.delete()
        self.up2.delete()
        self.t1.delete()
        self.t2.delete()
        self.ev1.delete()

