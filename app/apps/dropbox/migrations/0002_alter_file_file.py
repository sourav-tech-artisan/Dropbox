# Generated by Django 5.1.1 on 2024-09-08 14:40

import app.apps.base.utils.file_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=255, upload_to=app.apps.base.utils.file_storage.upload_file_path),
        ),
    ]
