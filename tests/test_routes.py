from django.test import Client, TestCase
from django.core.urlresolvers import reverse

class RoutesTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_route(self):
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)

    def test_events_route(self):
        response = self.client.get(reverse('Events'))
        self.assertEqual(response.status_code, 200)

    def test_about_route(self):
        response = self.client.get(reverse('About'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_route(self):
        response = self.client.get(reverse('Sign Up'))
        self.assertEqual(response.status_code, 200)

    def test_log_in_route(self):
        response = self.client.get(reverse('Log In'))
        self.assertEqual(response.status_code, 200)

    def test_log_out_route(self):
        response = self.client.get(reverse('Log Out'))
        self.assertEqual(response.status_code, 200)
