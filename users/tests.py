from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        # Given
        user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'nickname': 'testnick',
            'name': 'Test User',
            'phone_number': 1234567890,
            'staff': False,
            'admin': False,
            'is_activate': True
        }

        # When
        user = User.objects.create(**user_data)

        # Then
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.nickname, 'testnick')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.phone_number, 1234567890)
        self.assertFalse(user.staff)
        self.assertFalse(user.admin)
        self.assertTrue(user.is_activate)

    def test_user_str_method(self):
        # Given
        user = User.objects.create(email='test@example.com', name='Test User')

        # When
        user_str = str(user)

        # Then
        self.assertEqual(user_str, 'Test User')