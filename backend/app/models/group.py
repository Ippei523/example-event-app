from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=255, null= False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
