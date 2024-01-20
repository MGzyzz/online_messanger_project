from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    profile_pictures = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='profile_pics/default.png')

    STATUS_CHOICE = (('online', 'Онлайн'), 
                    ('away', 'Отошел')
                    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='online')