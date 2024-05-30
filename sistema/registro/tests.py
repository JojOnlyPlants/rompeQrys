from django.test import TestCase
from .models import Cuenta
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        exists = Cuenta.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)