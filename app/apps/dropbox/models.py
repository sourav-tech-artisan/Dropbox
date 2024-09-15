from django.db import models
from app.apps.base.models import TimeStampedUUIDModel
from app.apps.base.utils.file_storage import upload_file_path

# models are defined here

class File(TimeStampedUUIDModel):
    file = models.FileField(upload_to=upload_file_path, max_length=255)
    file_name = models.CharField(max_length=255, default='Untitled')
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'