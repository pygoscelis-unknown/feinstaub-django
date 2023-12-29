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

python --version
django-admin --version

### Installation

```bash
git clone https://github.com/username/project.git

cd project

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# start the development server
python manage.py runserver
```

## Usage

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

## Contributing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
