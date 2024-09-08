# Problem
The goal of this project is to implement a simplified Dropbox-like service where users can upload, retrieve, and
manage their files through a set of RESTful APIs. The service should also support the storage of metadata for each
uploaded file, such as the file name, creation timestamp, and more.

# Directory Structure
```
.
├── pyproject.toml            # Poetry file specifying Python dependencies
├── poetry.lock               # Poetry lock file specifying exact versions of dependencies
├── README.md                 # Markdown file containing project documentation
├── manage.py                 # Django management script for running administrative tasks
|── .env                      # Environment variables file
├── env.example               # Environment variables example file
├── .gitignore                # Git ignore file for specifying files and directories to ignore
├── secret.json               # Secret file for storing secret key and other sensitive information
├── docker                    # Directory containing Docker configuration files
│   ├── docker-compose.yml    # Docker Compose file for defining multi-container Docker applications
├── app                       # Django root application directory
│   ├── __init__.py           # Initialization file
│   ├── asgi.py               # ASGI configuration for the Django application
│   ├── settings.py           # Django settings file for application configuration
│   ├── urls.py               # Django URL configuration file
│   └── wsgi.py               # WSGI configuration for the Django application
│   ├── apps                  # Package containing application dependencies
│   │   ├── base              # base app for common functionalities
│   │   |   ├── __init__.py   # Initialization file
│   │   |   ├── migrations    # Directory containing database migration files
│   │   |   ├── models.py     # Django models file for defining database models
│   │   |   ├── serializers.py # Django serializers file for serializing data
│   │   |   ├── tests         # tests folder for testing application functionalities
│   │   |   └── viewsets.py   # Django viewssets file for defining API views
│   │   |   └── admin.py      # Django admin file for registering models with the admin interface
│   │   |   └── utils         # utils folder for common utility functions
│   │   |   └── apps.py       # Django apps file for application configuration
│   │   |   └── exceptions.py # exceptions file for handling exceptions
│   │   |   └── pagination.py # Base pagination logic for pagination
│   │   ├── dropbox           # dropbox app for file upload and download functionalities
│   │   |   ├── __init__.py   # Initialization file
│   │   |   ├── migrations    # Directory containing database migration files
│   │   |   ├── models.py     # Django models file for defining database models
│   │   |   ├── serializers.py # Django serializers file for serializing data
│   │   |   ├── tests         # tests folder for testing application functionalities
│   │   |   └── viewsets.py   # Django viewssets file for defining API views
│   │   |   └── admin.py      # Django admin file for registering models with the admin interface
│   │   |   └── apps.py       # Django apps file for application configuration
│   │   |   └── exceptions.py # exceptions file for handling exceptions
│   │   |   └── services      # services folder for business logic
│   │   |   └── repositories  # repositories folder for database operations
│   │   |   └── utils         # utils file for common utility functions
│   │   |   └── urls          # urls file for defining urls

```

# Running the project

To run the project locally -

```
1. Install poetry
2. Run `poetry install` to install dependencies, this will create poetry.lock file
3. Setup environment variables in .env file in root folder
4. Setup secret key in secret.json file in root folder
5. Database setup: 
    - Run 'docker compose -f docker/docker-compose.local.yml up -d' to start the database
    - Run 'poetry run python manage.py migrate' to apply migrations
6. Run `poetry run python manage.py runserver` to start the Django development server
```

## Run Unit Tests for dropbox app
```
poetry run python manage.py test app/apps/dropbox/tests
```

## Endpoints for dropbox app
```
1. Upload File: POST /dropbox/api/v1/files/
    Sample Request Body: 
        {
            "file": <file>,
            "file_name": "file_name"
        }
2. Get File by id: GET /dropbox/api/v1/files/{file_id}/
3. Get File List: GET /dropbox/api/v1/files/
4. Update File: PATCH /dropbox/api/v1/files/{file_id}/
    Sample Request Body: 
        {
            "file": <file> (optional),
            "file_name": "new_file_name" (optional),
        }
5. Delete File: DELETE /dropbox/api/v1/files/{file_id}/
```

