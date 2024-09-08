from django.contrib import admin
from app.apps.dropbox.repositories.dropbox_repo import DropboxRepo
from app.apps.base.admin import BaseModelAdmin

# models are registered here

@admin.register(DropboxRepo.get_model())
class DropboxModelAdmin(BaseModelAdmin):
    """Dropbox model admin class"""
    
    list_display = ('id', 'file_name',)
    search_fields = ('id', 'file_name',)
