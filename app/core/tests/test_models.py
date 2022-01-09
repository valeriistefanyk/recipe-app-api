from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

TEST_PASSWORD = "TestPass123"


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        user = User.objects.create(email=email)
        user.set_password(TEST_PASSWORD)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(TEST_PASSWORD))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = User.objects.create_user(email=email)
        user.set_password(TEST_PASSWORD)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, TEST_PASSWORD)

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser("test@gmail.com", TEST_PASSWORD)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
