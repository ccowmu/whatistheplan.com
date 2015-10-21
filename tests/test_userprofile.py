from django.test import Client, TestCase
from whatistheplan.models import UserProfile
from django.contrib.auth.models import User

class UserProfileTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user('username', 'email@email.com', 'password')
        self.u2 = User.objects.create_user('dickweed', 'email2@email.com', 'password')
        self.up1 = UserProfile.objects.create(user=self.u1, name="Lil Jon")
        self.up2 = UserProfile.objects.create(user=self.u2, name="dan", steamid="dyladan")

    def test_user_profile_ownership(self):
        """User - UserProfile is 1 to 1"""
        self.assertEqual(self.up1.user, self.u1)
        self.assertEqual(self.up2.user, self.u2)
        self.assertEqual(self.u1.userprofile, self.up1)
        self.assertEqual(self.u2.userprofile, self.up2)

    def test_user_autonumber_id(self):
        """Users being assigned IDs"""
        self.assertEqual(self.u1.id, 1)
        self.assertEqual(self.u2.id, 2)

    def tearDown(self):
        self.up1.delete()
        self.up2.delete()
        self.u1.delete()
        self.u2.delete()
