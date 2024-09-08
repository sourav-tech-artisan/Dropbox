from django.contrib import admin

# models are registered here

class BaseModelAdmin(admin.ModelAdmin):
    """Base Model Admin class to be inherited by other model admin classes"""

    readonly_fields = ('id', 'created_at', 'modified_at')