from django.db import models

from .user import User
from .tag import Tag


class Event(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null= True)
    description = models.CharField(max_length=255, null= True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    title = models.CharField(max_length=255, null= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
