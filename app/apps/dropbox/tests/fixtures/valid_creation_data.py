from django.core.files.uploadedfile import SimpleUploadedFile

VALID_CREATION_DATA = [
    {
        'file': SimpleUploadedFile("new_test_file.txt", b"New test file content"),
        'file_name': 'new_test_file.txt'
    },
    {
        'file': SimpleUploadedFile("new_test_file.pdf", b"New test file content"),
        'file_name': 'new_test_file.pdf',
    }
]