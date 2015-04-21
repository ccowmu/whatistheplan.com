from django.test import TestCase, Client
from whatistheplan.forms import UserForm, UserProfileForm

class UserFormTest(TestCase):
    def setUp(self):
        self.user_form_data = {
            'username': 'sn1par_eugene',
            'password': 'bloxwich',
            'email': 'h00bastankR0x@aol.com'
        }
        self.user_profile_form_data = {
            'name': "Eugene M'TnDew",
            'mac_address': '00:00:00:00i:00:00',
            'steamid': 'xXx_sn1par_eugene_420_xXx',
            'irc': 'eugene'
        }
        self.form_data = self.user_form_data.copy()
        self.form_data.update(self.user_profile_form_data)
        self.client = Client()

    def test_user_form_is_valid(self):
        """sample data is valid for user form"""
        form = UserForm(data=self.user_form_data)
        self.assertEqual(form.is_valid(), True)

    def test_user_profile_form_is_valid(self):
        """sample data is valid for user profile form"""
        form = UserProfileForm(data=self.user_profile_form_data)
        self.assertEqual(form.is_valid(), True)

    def test_user_form_submission_success(self):
        """form submission with sample data success"""
        resp = self.client.post("/signup/", self.form_data)
        self.assertEqual(resp.status_code, 200)

