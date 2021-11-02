from django.db import models
from django.contrib.auth.models import User

class ChatMessages(models.Model):
    sender = models.CharField(max_length=60)
    room_name = models.CharField(max_length=60)
    message = models.TextField()
    timestamp = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
