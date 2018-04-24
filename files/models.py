from uuid import uuid4
from django.db import models

# Create your models here.
class File(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=64)
  upload = models.FileField(upload_to='uploads/')
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
