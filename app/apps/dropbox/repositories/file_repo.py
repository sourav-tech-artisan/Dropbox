from django.db.models.query import QuerySet
from app.apps.dropbox.models import File
from app.apps.base.exceptions import InternalServerError
from app.apps.dropbox.exceptions import DataIntegrityError, FileDoesNotExistError, MultipleObjectsReturnedError, InvalidDataError
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError


class FileRepo:
    """File Repository
    
    This class is responsible for handling all the database interactions for the File.

    Methods defined here:
    - get_model() -> File: Returns File model class
    - get_all_queryset() -> QuerySet[File]: Returns a queryset containing all the file objects
    - create_file(data) -> File: Creates File
    - get_file_by_id(file_id) -> File: Returns a file object by id
    """

    @classmethod
    def get_model(cls) -> File:
        """Returns File model class"""
        return File
    
    @classmethod
    def get_all_queryset(cls) -> QuerySet[File]:
        """Returns a queryset containing all the file objects"""
        try:
            return cls.get_model().objects.all()
        except Exception as e:
            raise InternalServerError(f"Error occurred while fetching files: {str(e)}")
    
    @classmethod
    def create_file(cls, **data) -> File:
        """Creates File
        Args:
            data (dict): The data to create a new file
        
        Returns:
            File: The created file
        """
        try:
            file = cls.get_model().objects.create(**data)
            return file
        except IntegrityError as e:
            raise DataIntegrityError(f"Error occurred while creating file: {str(e)}")
        except ValidationError as e:
            raise InvalidDataError()
        except Exception as e:
            raise InternalServerError(f"Error occurred while creating file: {str(e)}")
        
    @classmethod
    def get_file_by_id(cls, file_id) -> File:
        """Returns a file object by id
        Args:
            file_id (uuid): The id of the file
        
        Returns:
            File: The file object
        """
        try:
            return cls.get_model().objects.get(id=file_id)
        except ObjectDoesNotExist:
            raise FileDoesNotExistError()
        except MultipleObjectsReturned:
            raise MultipleObjectsReturnedError()
        except Exception as e:
            raise InternalServerError(f"Error occurred while fetching file with id {file_id}: {str(e)}")
        
    
    