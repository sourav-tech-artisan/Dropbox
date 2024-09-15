from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, status


class BaseException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Unexpected error")

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail

class NotFound(BaseException, Http404):
    """Exception used for objects not found."""

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Not found.")

class NotSupported(BaseException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = _("Method not supported for this endpoint.")

class InternalServerError(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("Internal Server Error")

class BadRequest(BaseException):
    """Exception used on bad arguments detected on api view."""

    default_detail = _("Wrong arguments.")
