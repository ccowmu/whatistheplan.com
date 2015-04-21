from django.test import TestCase
from whatistheplan.forms import UserForm, UserProfileForm

class UserFormTest(TestCase):
    def test_user_form(self):
        form_data = {
            'username': 'sn1par_eugene',
            'password': 'bloxwich',
            'email': 'h00bastankR0x@aol.com'
        }
        form = UserForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_user_profile_form(self):
        form_data = {
            'name': "Eugene M'TnDew",
            'mac_address': '00:00:00:00i:00:00',
            'steamid': 'xXx_sn1par_eugene_420_xXx',
            'irc': 'eugene'
        }
        form = UserProfileForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

