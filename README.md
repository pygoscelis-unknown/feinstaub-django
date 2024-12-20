# Feinstaub API - Django

## Table of Contents

-   [Project Overview](#project-overview)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
        -   [Clone repository](#clone-repository)
        -   [Install dependencies](#install-dependencies)
        -   [Add environment variables](#add-environment-variables)
-   [Usage](#usage)
    -   [Start the development server](#start-the-development-server)
    -   [Apply migrations](#apply-migrations)
    -   [Get data header from csv files](#get-data-header-from-csv-files)
    -   [Generate base files for your app](#generate-base-files-for-your-app)
    -   [Import data from csv files to database](#import-data-from-csv-files-to-database)
-   [Configuration](#configuration)
-   [Contributing](#contributing)
-   [License](#license)
-   [Acknowledgments](#acknowledgments)

## Project Overview

## Getting Started

### Prerequisites
- Python 3
```bash
python3 --version
```

### Installation

#### Clone repository
```bash
git clone https://github.com/pygoscelis-unknown/feinstaub-django.git
cd feinstaub-django
```

#### Install dependencies
```bash
pip3 install -r requirements.txt
```

#### Add environment variables
- copy .env.example to .env and set your database
    ```
    DB_ENGINE=<DATABASE_ENGINE>
    POSTGRES_DB=<DATABASE_NAME>
    POSTGRES_USER=<DATABASE_USER>
    POSTGRES_PASSWORD=<DATABASE_PASSWORD>
    DB_HOST=<DATABASE_HOST> # set in docker-compose.yaml when using docker
    DB_PORT=<DATABASE_PORT>
    
    DJANGO_SECRET_KEY=<DJANGO_SECRET_KEY>
    DJANGO_PROJECT_NAME="feinstaub"
    DJANGO_APP_NAME="importer"
    
    SENSOR_ARCHIVE_URL="http://archive.sensor.community"
    ```
- add your own secret key - you can generate a secret key with the following command:
    ```bash
    django-admin shell
    ```
    then in python shell:
    ```python
    from django.core.management.utils import get_random_secret_key
    get_random_secret_key()
    ```

## Usage
### Start the development server
```bash
python manage.py runserver
```

### Get data header from csv files
```bash
python manage.py get_csv_header --date <YYYY-MM-DD>
```
This script generates `./sensor_csv_header.json`.

### Generate base files for your app
```bash
python manage.py generate_base_files --json ./sensor_csv_header.json
```
This script generates the following files:
- models.py
- admin.py
- serializers.py
- views.py
- urls.py

    in `./importer`

- create_object.py

    in `./importer/management/commands/modules`

- urls.py

    in `./feinstaub`

### Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Import data from csv files to database
```bash
python manage.py import_data
```
All other commands can be found in `./importer/management/commands`.

## Configuration

## Deployment

## Further information
This project uses Django Rest Framework for the REST API.

## Contributing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.

## Acknowledgments

