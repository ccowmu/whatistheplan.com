from django.test import Client, TestCase
from whatistheplan.models import UserProfile
from django.contrib.auth.models import User

class MyTesting(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='dickweed')
        self.u2 = User.objects.create(username='jack',)
        self.up1 = UserProfile.objects.create(user=self.u1, name="dan", email="dyladan@gmail.com")
        self.up2 = UserProfile.objects.create(user=self.u2, name="jack", email="jack@yakko.cs.wmich.edu")

    def test_user_profile_ownership(self):
        self.assertEqual(self.up1.user, self.u1)
        self.assertEqual(self.up2.user, self.u2)

    def test_user_autonumber_id(self):
        self.assertEqual(self.u1.id, 1)
        self.assertEqual(self.u2.id, 2)

    def tearDown(self):
        self.up1.delete()
        self.up2.delete()
        self.u1.delete()
        self.u2.delete()
