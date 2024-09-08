from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from app.apps.dropbox.repositories.file_repo import FileRepo
from app.apps.dropbox.tests.endpoints import CREATE_FILE_URL, GET_FILE_URL, UPDATE_FILE_URL, LIST_FILES_URL, DELETE_FILE_URL
from app.apps.dropbox.tests.fixtures.valid_creation_data import VALID_CREATION_DATA
from app.apps.dropbox.tests.fixtures.invalid_creation_data import INVALID_CREATION_DATA
from app.apps.dropbox.tests.fixtures.valid_updation_data import VALID_UPDATION_DATA

class FilesAPITestCase(APITestCase):
    def setUp(self):
        fields = {
            "file": SimpleUploadedFile("test_file.txt", b"Test file content"),
            "file_name": "test file name",
        }
        url = CREATE_FILE_URL
        self.client.post(url, fields, format='multipart')
        self.test_file = FileRepo.get_all_queryset().latest('created_at')

    def test_create_file_with_valid_data(self):
        """Test creating a new file."""
        url = CREATE_FILE_URL
        # count of files created
        count = 1 # 1 file created in setUp
        for data in VALID_CREATION_DATA:
            response = self.client.post(url, data, format='multipart')
            count += 1
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # check that the file was created with correct file name
            self.assertEqual(FileRepo.get_all_queryset().count(), count)
            new_file = FileRepo.get_all_queryset().latest('created_at')
            self.assertEqual(new_file.file_name, data.get("file_name"))
            # check that file size and file type were added to the file
            self.assertTrue(new_file.file_size)
            self.assertTrue(new_file.file_type)
            self.assertTrue(new_file.file)
            self.assertTrue(new_file.file_name)
            self.assertTrue(new_file.created_at)
            self.assertTrue(new_file.modified_at)

    def test_create_file_with_invalid_data(self):
        """Test creating a new file with invalid data."""
        url = CREATE_FILE_URL
        # count of files created
        count = 1
        for data in INVALID_CREATION_DATA:
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            # check that the file was not created
            self.assertEqual(FileRepo.get_all_queryset().count(), count)

    def test_retrieve_file(self):
        """Test retrieving a file."""
        file_id = str(self.test_file.id)
        url = GET_FILE_URL.format(file_id=file_id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("file_name"), "test file name")
        self.assertEqual(response.data.get("file_size"), self.test_file.file_size)
        self.assertEqual(response.data.get("file_type"), self.test_file.file_type)
        self.assertEqual(response.data.get("file"), self.test_file.file.url)

    def test_list_files_without_pagination(self):
        """Test listing files without pagination."""
        url = LIST_FILES_URL + "?page_size=0"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIsInstance(response.data, list)

    def test_list_files_with_pagination(self):
        """Test listing files with pagination."""
        url = LIST_FILES_URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_update_file_with_valid_data(self):
        """Test updating a file."""
        file_id = str(self.test_file.id)
        url = UPDATE_FILE_URL.format(file_id=file_id)
        for data in VALID_UPDATION_DATA:
            response = self.client.patch(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            updated_file = FileRepo.get_file_by_id(file_id)
            if data.get("file"):
                self.assertTrue(updated_file.file)
            if data.get("file_name"):
                self.assertEqual(updated_file.file_name, data.get("file_name"))

    def test_update_file_with_invalid_data(self):
        """Test updating a file with invalid data."""
        file_id = str(self.test_file.id)
        url = UPDATE_FILE_URL.format(file_id=file_id)
        for data in INVALID_CREATION_DATA:
            response = self.client.patch(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            # check that the file was not updated
            updated_file = FileRepo.get_file_by_id(file_id)
            if data.get("file"):
                self.assertTrue(updated_file.file)
            if data.get("file_name"):
                self.assertNotEqual(updated_file.file_name, data.get("file_name"))

    def test_delete_file(self):
        """Test deleting a file."""
        file_id = str(self.test_file.id)
        url = DELETE_FILE_URL.format(file_id=file_id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # check that the file was deleted
        files = FileRepo.get_all_queryset()
        self.assertEqual(files.count(), 0)