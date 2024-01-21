from django.test import TestCase
from .models import Message, Chat
from accounts.models import User
import datetime
# Create your tests here.
class MessageTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.sender = User.objects.create_user(username='sender', password='test12345')
        cls.recipient = User.objects.create_user(username='recipient', password='test12345')
        cls.message = Message.objects.create(
            sender=cls.sender,
            recipient=cls.recipient,
            content='Hello!'
        )
    
    def test_message_creation(self):
        self.assertEqual(self.message.sender, self.sender)
        self.assertEqual(self.message.recipient, self.recipient)
        self.assertEqual(self.message.content, 'Hello!')
        self.assertIsInstance(self.message.timestamp, datetime.datetime)
        self.assertFalse(self.message.is_read)

    def test_message_str(self):
        expected_string = f'Message from {self.sender}, to {self.recipient}, sent at {self.message.timestamp}'
        self.assertEqual(str(self.message), expected_string)
    

class ChatModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username='user1', password='test12345')
        cls.user2 = User.objects.create_user(username='user2', password='test12345')
        cls.chat = Chat.objects.create()
        cls.chat.participants.set([cls.user1, cls.user2])
        cls.message = Message.objects.create(sender=cls.user1, recipient=cls.user2, content='Hello!')
        cls.chat.message.add(cls.message)

    def test_chat_creation(self):
        self.assertIn(self.user1, self.chat.participants.all())
        self.assertIn(self.user2, self.chat.participants.all())
        self.assertIn(self.message, self.chat.message.all())

    def test_chat_created_at(self):
        self.assertIsInstance(self.chat.created_at, datetime.datetime)

    def test_chat_str(self):
        expected_string = f'Chat with ID {self.chat.id} created at {self.chat.created_at}'
        self.assertEqual(str(self.chat), expected_string)