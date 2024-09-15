from rest_framework import serializers
from app.apps.base.serializers import DynamicFieldsSerializer
from app.apps.dropbox.repositories.file_repo import FileRepo
from app.settings import FILE_SIZE_LIMIT
import mimetypes


class FileCreateSerializer(serializers.ModelSerializer):
    """File create serializer class
    
    This class is responsible for serializing and validating the data for creating a new file request.
    """
    file = serializers.FileField()
    file_name = serializers.CharField(max_length=255, required=False, default='Untitled')

    def validate_file(self, value):
        """Validate file
        
        This method is responsible for validating the file size.
        
        Args:
            value (File): The file object
        
        Raises:
            serializers.ValidationError: If the file size is greater than the limit
        
        Returns:
            File: The file object
        """
        if value.size > FILE_SIZE_LIMIT:
            raise serializers.ValidationError('File size is too large')
        return value
    
    def validate(self, attrs):
        super().validate(attrs)
        # Add file size to attrs
        attrs['file_size'] = attrs['file'].size
        # Add file type to attrs
        attrs['file_type'] = mimetypes.guess_type(attrs['file'].name)[0] or 'unknown'

        return attrs

    class Meta:
        model = FileRepo.get_model()
        fields = ('file', 'file_name')


class FileUpdateSerializer(serializers.ModelSerializer):
    """File update serializer class
    
    This class is responsible for serializing and validating the data for updating a file.
    """
    file = serializers.FileField(required=False)
    file_name = serializers.CharField(max_length=255, required=False)

    def validate_file(self, value):
        """Validate file
        
        This method is responsible for validating the file size.
        
        Args:
            value (File): The file object
        
        Raises:
            serializers.ValidationError: If the file size is greater than the limit
        
        Returns:
            File: The file object
        """
        if value.size > FILE_SIZE_LIMIT:
            raise serializers.ValidationError('File size is too large')
        return value
    
    def validate(self, attrs):
        super().validate(attrs)
        # Add file size and file type to attrs
        if 'file' in attrs:
            attrs['file_size'] = attrs['file'].size
            # Add file type to attrs
            attrs['file_type'] = mimetypes.guess_type(attrs['file'].name)[0] or 'unknown'

        return attrs
    class Meta:
        model = FileRepo.get_model()
        fields = ('file', 'file_name',)


class FileReadSerializer(DynamicFieldsSerializer):
    """File read serializer class
    
    This class is responsible for serializing the data for reading a file.
    """
    class Meta:
        model = FileRepo.get_model()
        fields = '__all__'