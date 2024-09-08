from app.apps.base.exceptions import BadRequest
from django.utils.translation import gettext_lazy as _

class DataIntegrityError(BadRequest):
    """DataIntegrityError
    This exception is raised when there is a data integrity error.
    """
    default_detail = _('Data integrity error.')

class FileDoesNotExistError(BadRequest):
    """FileDoesNotExistError
    This exception is raised when the file does not exist.
    """
    default_detail = _('File with this id does not exist.')

class MultipleObjectsReturnedError(BadRequest):
    """MultipleObjectsReturned
    This exception is raised when multiple objects are returned.
    """
    default_detail = _('Multiple objects returned.')

class InvalidDataError(BadRequest):
    """InvalidDataError
    This exception is raised when the data provided is invalid.
    """
    default_detail = _('Invalid data provided.')

