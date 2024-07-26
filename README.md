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
python --version
```

### Installation

#### Clone repository
```bash
git clone https://github.com/pygoscelis-unknown/django-feinstaub.git
```
```bash
cd django-feinstaub
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Add environment variables
- copy .env.example to .env and set your database data
- add your own secret key


## Usage
### Start the development server
```bash
python manage.py runserver
```

### Apply migrations
```bash
python manage.py migrate
```

### Get data header from csv files
```bash
python manage.py get_csv_header --date <YYYY-MM-DD>
```
This script generates in your project root sensor_csv_header.json with all sensor types on target link and all header data of each sensor type. The date of the most recent csv file should be used.

### Generate base files for your app
```bash
python manage.py generate_base_files --json <PROJECT_ROOT>/sensor_csv_header.json --project <PROJECT_NAME> --app <APP_NAME>
```
This scripts generate the following files:
- models.py
- admin.py
- serializers.py
- views.py
- urls.py

    in `<APP_ROOT>/`

- create_object.py

    in `<APP_ROOT>/management/commands/modules/`

- urls.py

    in `<PROJECT_ROOT>/`

### Import data from csv files to database
to get data of all sensor types available in zip format for one month from zipped csv files
```bash
python manage.py import_data-zip-all-multiprocessing --year <YYYY> --month <MM> --app <APP_NAME>
```
to get data of a specific sensor type available in zip format for one month from zipped csv files
```bash
python manage.py import_data-zip-mono-multiprocessing --year <YYYY> --month <MM> --type <SENSOR_TYPE>
```
Other available commands are to find in `<APP_ROOT>/management/commands/`.

## Configuration

## Deployment

## Further information
This project uses DRF (Django Rest Framework) for the REST API. 

## Contributing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

