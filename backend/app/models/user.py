from django.db import models

from .group import Group


class User(models.Model):
    name = models.CharField(max_length=255, null=False, db_index=True)
    tel_number = models.CharField(max_length=255, null=False, db_index=True)
    email = models.CharField(max_length=255, null=False, db_index=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
