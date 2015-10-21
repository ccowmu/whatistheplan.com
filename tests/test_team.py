from django.test import Client, TestCase
from whatistheplan.models import Team, Game, UserProfile
from django.contrib.auth.models import User

class TeamTest(TestCase):
    def setUp(self):
        self.g1 = Game.objects.create(game_name='Counter Strike Source')
        self.g1.save()

        self.u1 = User.objects.create_user('username', 'email@email.com', 'password')
        self.u2 = User.objects.create_user('dickweed', 'email2@email.com', 'password')
        self.u1.save()
        self.u2.save()

        self.up1 = UserProfile.objects.create(user=self.u1, name="Lil Jon")
        self.up2 = UserProfile.objects.create(user=self.u2, name="dan", steamid="dyladan")
        self.up1.save()
        self.up2.save()

        self.t1 = Team.objects.create(team_name='The Crows', game=self.g1)
        self.t2 = Team.objects.create(team_name='Wildlings', game=self.g1)
        self.t1.save()
        self.t2.save()

    def test_team_game_relationship(self):
        """Each game should be played by many teams"""
        self.assertEqual(self.g1.game_name, 'Counter Strike Source')
        self.assertEqual(self.t1.game, self.g1)
        self.assertEqual(self.t2.game, self.g1)

    def test_many_userprofiles_per_team(self):
        """Team owns many userprofiles"""
        self.t1.userprofiles.add(self.up1)
        self.t1.userprofiles.add(self.up2)

    def test_many_teams_per_userprofile(self):
        """userprofiles on many teams"""
        self.t1.userprofiles.add(self.up1)
        self.t2.userprofiles.add(self.up1)

    def tearDown(self):
        self.g1.delete()

        self.t1.delete()
        self.t2.delete()

        self.up1.delete()
        self.up2.delete()

        self.u1.delete()
        self.u2.delete()
