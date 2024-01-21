from django.db import models
from django.conf import settings
from .message import Message

class Chat(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')
    message = models.ManyToManyField(Message, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Chat with ID {self.id} created at {self.created_at}'