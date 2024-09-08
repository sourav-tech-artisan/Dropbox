from app.apps.dropbox.repositories.file_repo import FileRepo
from app.apps.base.exceptions import InternalServerError

class FileService:
    """File Service
    
    This class is responsible for handling all the business logic for File.

    Methods defined here:
    - create_file(data) -> File: Create File
    - update_file(instance, data) -> File: Update File
    """

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
        