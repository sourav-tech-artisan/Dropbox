from django.core.files.uploadedfile import SimpleUploadedFile
# invalid data
INVALID_CREATION_DATA = [
    {
        "file": "invalid_test_file.txt",
    },
    {
        "file": SimpleUploadedFile("invalid_test_file.pdf", b"Invalid test file content"),
        "file_name": SimpleUploadedFile("invalid_test_file.pdf", b"Invalid test file content"),
    }
]