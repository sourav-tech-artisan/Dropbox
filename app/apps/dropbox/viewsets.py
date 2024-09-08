from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from app.apps.dropbox.repositories.file_repo import FileRepo
from app.apps.base.pagination import StandardResultsSetPagination
from app.apps.dropbox.serializers import FileCreateSerializer, FileReadSerializer
from app.apps.base.exceptions import NotSupported
from app.apps.dropbox.services.file_service import FileService
from app.apps.dropbox.utils import filter_response_fields


class FileViewSet(viewsets.ModelViewSet):
    """Dropbox viewset.
    
    This class is responsible for handling all the API requests that are related to the Files.
    
    Endpoints implemented here:
    - POST /files/ - Create a new file
    - GET /files/{id}/ - Retrieve a file
    """

    queryset = FileRepo.get_all_queryset()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        """Get serializer class."""
        match self.action:
            case 'create':
                return FileCreateSerializer
            case 'retrieve':
                return FileReadSerializer
            case _:
                raise NotSupported()

    def create(self, request, *args, **kwargs):
        """Create a new file."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        file = FileService.create_file(data)
        file = FileReadSerializer(file).data
        return Response(file, status=201)
    
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a file."""
        instance = self.get_object()
        fields = filter_response_fields(model=FileRepo.get_model(),request=request)
        data = self.get_serializer(instance, fields=fields).data
        return Response(data, status=200)
        
        
        

