from django.core.files.uploadedfile import SimpleUploadedFile

VALID_UPDATION_DATA = [
    {
        'file': SimpleUploadedFile("updated_file1.txt", b"New test file content"),
        'file_name': 'updated1.txt'
    },
    {
        'file': SimpleUploadedFile("updated_file2.pdf", b"New test file content"),
    },
    {
        'file_name': 'updated.txt',
    }
]