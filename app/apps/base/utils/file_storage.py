from django.utils import timezone

def upload_file_path(instance, filename):
    """Returns a path to upload the file"""
    today = timezone.localtime(timezone.now()).date()
    folder_name = instance.id
    return f"{folder_name}/{today}/{filename}"