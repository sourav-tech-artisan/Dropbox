from app.apps.dropbox.repositories.file_repo import FileRepo
from app.apps.base.exceptions import InternalServerError
from google.cloud import storage
from app.settings import GS_BUCKET_NAME
class FileService:
    """File Service
    
    This class is responsible for handling all the business logic for File.

    Methods defined here:
    - __delete_file_from_storage(instance) -> None: Delete File From Storage
    - create_file(data) -> File: Create File
    - update_file(instance, data) -> File: Update File
    - delete_file(instance) -> None: Delete File
    """

    @classmethod
    def __delete_file_from_storage(cls, instance):
        """Delete File From Storage
        
        This method is responsible for deleting a file from storage.
        
        Args:
            instance (File): The file to delete
        """
        # TODO: Make this operation asynchronous/poll cloud storage for deletion of files
        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket(GS_BUCKET_NAME)
            blob = bucket.blob(str(instance.id))
            blob.delete()
        except Exception as e:
            raise InternalServerError(f"Error occurred while deleting file from Google Cloud Storage: {str(e)}")

    @classmethod
    def create_file(cls, data):
        """Create File
        
        This method is responsible for creating a new file.
        
        Args:
            data (dict): The data to create a new file
        
        Returns:
            File: The created file
        """
        return FileRepo.create_file(**data)
    
    @classmethod
    def update_file(cls, instance, data):
        """Update File
        
        This method is responsible for updating a file.
        
        Args:
            data (dict): The data to update a file
        
        Returns:
            File: The updated file
        """
        return FileRepo.update_file(instance, **data)
    
    @classmethod
    def delete_file(cls, instance):
        """Delete File
        
        This method is responsible for deleting a file.
        
        Args:
            instance (File): The file to delete
        """
        # Delete the file in cloud storage
        cls.__delete_file_from_storage(instance)
        # Delete the file in application DB
        FileRepo.delete_file(instance)


        