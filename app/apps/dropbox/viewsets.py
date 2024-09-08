from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from app.apps.dropbox.repositories.file_repo import FileRepo
from app.apps.base.pagination import StandardResultsSetPagination
from app.apps.dropbox.serializers import FileCreateSerializer, FileReadSerializer, FileUpdateSerializer
from app.apps.base.exceptions import NotSupported
from app.apps.dropbox.services.file_service import FileService
from app.apps.dropbox.utils import filter_response_fields


class FileViewSet(viewsets.ModelViewSet):
    """Dropbox viewset.
    
    This class is responsible for handling all the API requests that are related to the Files.
    
    Endpoints implemented here:
    - POST /files/ - Create a new file
    - GET /files/{id}/ - Retrieve a file
    - GET /files/ - List all files
    - PATCH /files/{id}/ - Update a file
    - DELETE /files/{id}/ - Delete a file
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
            case 'list':
                return FileReadSerializer
            case 'partial_update':
                return FileUpdateSerializer
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
    
    def list(self, request, *args, **kwargs):
        """List all files."""
        fields = filter_response_fields(model=FileRepo.get_model(),request=request)
        queryset = self.filter_queryset(self.get_queryset())
        pagination = int(request.query_params.get('page_size', 1) or 1)
        if not pagination:
            self._paginator = None
        page = self.paginate_queryset(queryset)
        if page is not None:
            data = self.get_serializer(page, fields=fields, many=True).data
            return self.get_paginated_response(data)
        data = self.get_serializer(queryset, fields=fields, many=True).data
        return Response(data, status=200)
    
    def partial_update(self, request, *args, **kwargs):
        """Updates a file."""
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        file = FileService.update_file(instance, data)
        file = FileReadSerializer(file).data
        return Response(file, status=200)
    
    def destroy(self, request, *args, **kwargs):
        """Deletes a file."""
        return super().destroy(request, *args, **kwargs)
        
        
        

