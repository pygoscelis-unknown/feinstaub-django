# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]