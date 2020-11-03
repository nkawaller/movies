from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()

        user = User.objects.create_user(
            username = 'nathan',
            email = 'nathan@email.com',
            password = 'nathanpass123'
        )

        self.assertEqual(user.username, 'nathan')
        self.assertEqual(user.email, 'nathan@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)



    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username = 'nathanadmin',
            email = 'nathanadmin@email.com',
            password = 'nathanpass123'
        )

        self.assertEqual(admin_user.username, 'nathanadmin')
        self.assertEqual(admin_user.email, 'nathanadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
