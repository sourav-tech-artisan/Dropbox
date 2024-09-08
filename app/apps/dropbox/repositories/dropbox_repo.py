from app.apps.dropbox.models import File


class DropboxRepo:
    """Dropbox Repository
    
    This class is responsible for handling all the database operations for the Dropbox app.
    """

    @classmethod
    def get_model(cls):
        """Get Model
        
        This method returns the model for the Dropbox app.
        
        Returns:
            File: The model for the Dropbox app.
        """
        return File
    
    @classmethod
    def get_all_queryset(cls):
        """Get All Queryset
        
        This method returns all the files from the database.
        
        Returns:
            QuerySet[File]: The queryset containing all the files.
        """
        return cls.get_model().objects.all()
    