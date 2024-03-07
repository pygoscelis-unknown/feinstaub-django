# feinstaub.app

## Table of Contents

-   [Project Overview](#project-overview)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
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
django-admin --version
```

### Installation

__Clone repository__
```bash
git clone https://github.com/username/project.git
```

```bash
cd django-feinstaub
```

__Install dependencies__
```bash
pip install -r requirements.txt
```

__Add environment variables__
- copy .env.example to .env
- add secrets


## Usage
### Start the development server
```bash
python manage.py runserver
```

### Apply migrations
```bash
python manage.py migrate
```



1. get data header from csv files
```
python manage.py get_csv_header-v4 --url {url} --date {date}
```
this script generates sensor_csv_header.json with all sensor types on target link and all header data of each sensor type

2. generate models.py, admin.py and create_object.py
```
python manage.py generate_models --path sensor_csv_header.json
```
generated script must be moved to apropriate location for next step:
- models.py, admin.py to target app's root (override existing models.py, admin.py)
- create_object.py to management/commands/modules/ of target app

3. import data from csv files to database
```
python manage.py import_data-v4 --url {url}
```
This currently fetchs data of yesterday.
!IS STILL BUGGY! has issues with some timestamps etc.

## Configuration

## Deployment
This app is deployed to render.com. As a build command render uses the `build.sh` script to install dependencies and run migrations.

Render provides an internal and external database connection string. We use a configuration based on the external connection string.

## Further information
This project uses DRF (Django Rest Framework) for the REST API. 

## Contributing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
