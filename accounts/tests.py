from django.test import TestCase
from .models import User
# Create your tests here.


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser', email='test@example.com', status='online')

    def test_email_label(self):
        field_label = self.user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email address')

    def test_max_length_username(self):
        max_length = self.user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150)

    def test_email_label_fail(self):
        max_length = self.user._meta.get_field('username').max_length
        self.assertEqual(max_length, 10)

    def test_status_choice_label(self):
        expected_choices = (
            ('online', 'Онлайн'), 
            ('away', 'Отошел')
        )
        self.assertEqual(User.STATUS_CHOICE, expected_choices)

    def test_status_field_saves_correct_value(self):
        self.assertEqual(self.user.status, 'online')
    
    def test_status_field_rejects_invalid_value(self):
        with self.assertEqual(ValueError):
            self.user.status = 'Invalid Status'
            self.user.full_clean()