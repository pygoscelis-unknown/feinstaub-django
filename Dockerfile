# pull official base image
FROM FROM python:3

# set work directory
WORKDIR /usr/src/app

COPY . .

# install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python manage.py get_csv_header --date 2024-06-01 && \
    python manage.py generate_base_files --json ./sensor_csv_header.json --project django_feinstaub --app test_app && \
    python manage.py makemigrations && \
    python manage.py migrate
