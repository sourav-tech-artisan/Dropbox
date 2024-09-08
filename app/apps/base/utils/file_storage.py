from django.utils import timezone

def upload_file_path(instance, filename):
    """Returns a path to upload the file"""
    folder_name = str(instance.id)
    return folder_name