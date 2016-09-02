from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

class RoutesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logged_in_client = Client()
        self.user = User.objects.create_user("testuser", "test@email.com", "test_password")
        self.logged_in_client.login(username="testuser", password="test_password")

    def test_home_route(self):
        """Home returns 200"""
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)

    def test_events_route(self):
        """Events returns 200"""
        response = self.client.get(reverse('Events'))
        self.assertEqual(response.status_code, 200)

    def test_about_route(self):
        """About returns 200"""
        response = self.client.get(reverse('About'))
        self.assertEqual(response.status_code, 200)

    def test_twitch_route(self):
        response = self.client.get(reverse('Twitch'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_route(self):
        """Sign Up returns 200"""
        response = self.client.get(reverse('Sign Up'))
        self.assertEqual(response.status_code, 200)

    def test_log_in_route(self):
        """Log in returns 200"""
        response = self.client.get(reverse('Log In'))
        self.assertEqual(response.status_code, 200)

    def test_log_out_route_for_logged_in_user(self):
        """Log Out redirects home for a logged in user"""
        response = self.logged_in_client.get(reverse('Log Out'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], 'http://testserver/')

    def tearDown(self):
        self.user.delete()
