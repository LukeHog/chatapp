from django.db import models

class ChatMessages(models.Model):
    sender = models.CharField(max_length=60)
    room_name = models.CharField(max_length=60)
    message = models.TextField()
    timestamp = models.DateTimeField()
