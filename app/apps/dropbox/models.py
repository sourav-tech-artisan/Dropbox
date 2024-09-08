from django.db import models
from app.apps.base.models import TimeStampedUUIDModel

# models are defined here

class File(TimeStampedUUIDModel):
    file = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=255, default='Untitled')
    file_size = models.IntegerField()

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'