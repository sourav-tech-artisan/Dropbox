from django.contrib import admin
from app.apps.dropbox.repositories.file_repo import FileRepo
from app.apps.base.admin import BaseModelAdmin

# models are registered here

@admin.register(FileRepo.get_model())
class FileModelAdmin(BaseModelAdmin):
    """Dropbox model admin class"""
    
    list_display = ('id', 'file_name',)
    search_fields = ('id', 'file_name',)
