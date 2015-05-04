from django.contrib.auth import authenticate, login
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from whatistheplan.models import UserProfile

class TestAuth(TestCase):
    def test_sign_up(self):
        """Test valid sign up"""
        response = self.client.post(reverse('Sign Up'), {
            'name': "Eugene M'TnDew",
            'username': 'sn1par',
            'password': 'bloxwich',
            'email': 'h00bastank_r0x@aol.com',
            'mac_address': '00:00:00:00:00:00',
            'steamid': 'xXx_sn1par_eugene_xXx',
            'irc': 'eugene'
            }, follow=True)
        # A valid sign up will redirect us to /login/
        self.assertRedirects(response,
            reverse('Log In'),
            status_code=302,
            target_status_code=200,
            )

        # Now, test logging as the user
        response = self.client.post(reverse('Log In'), {
            'username': 'sn1par',
            'password': 'bloxwich'
            }, follow=True)
        # A valid log in will redirect us to /
        self.assertRedirects(response,
            reverse('Home'),
            status_code=302,
            target_status_code=200,
            )

    def test_inactive_log_in(self):
        """Test that inactive accounts aren't able to log in"""
        # Create a user
        response = self.client.post(reverse('Sign Up'), {
            'name': "Billy Bob",
            'username': 'quickscopr420',
            'password': 'doritosfedoraeuphoria',
            'email': 'quickscopr420@aol.com',
            'mac_address': '00:00:00:00:00:00',
            'steamid': 'billybob',
            'irc': 'billybob'
            }, follow=True)

        # Disable the user
        bill = User.objects.get(username='quickscopr420')
        bill.is_active = False
        bill.save()

        # Check the response
        response = self.client.post(reverse('Log In'), {
            'username': 'quickscopr420',
            'password': 'doritosfedoraeuphoria'
            }, follow=True)
        self.assertContains(response, text='user is inactive, please talk to an admin.')

    def test_invalid_log_in(self):
        """Test invalid log in, the user will not exist"""
        response = self.client.post(reverse('Log In'), {
            'username': 'sn1par',
            'password': 'bloxwich'
            })
        self.assertContains(response, text='invalid credentials!')
