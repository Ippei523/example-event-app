from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=255, null= False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
