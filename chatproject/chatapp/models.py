from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class ChatMessages(models.Model):
    sender = models.CharField(max_length=60)
    room_name = models.CharField(max_length=60)
    message = models.TextField()
    timestamp = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

#class User(AbstractUser):
#    last_login = models.DateTimeField(blank=True, null=True)

#    def is_online(self):
#        if self.last_online:
#            return (timezone.now() - self.last_online) < timezone.timedelta(minutes=15)
#        return False