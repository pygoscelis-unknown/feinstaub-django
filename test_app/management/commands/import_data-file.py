from django.core.management import BaseCommand
import csv

from bs4 import BeautifulSoup
import requests
import urllib.request
import datetime
import time
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create

# command example
# python manage.py import_data-file --path path/to/file 

class Command(BaseCommand):
    help = 'Load data from local csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
        parser.add_argument('--date', type=str)
        parser.add_argument('--type', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        sensor_type = kwargs['type']

        start = time.time()
        object_count = 0

        with open(path) as file:
            lines = file.readlines()

        reader = csv.reader(lines, delimiter=";")

        index = 0
        header = []

        for row in reader:
            # ignore first header row
            if index == 0:
                for i in range(len(row)):
                    header.append(row[i])
                index += 1

            else:
                # ignore/convert illigal values
                for i in range(len(row)):
                    if header[i] != "sensor_type":
                        if header[i] == "sensor_id" or header[i] == "location":
                            #int
                            try:
                                row[i] = int(row[i])
                            except ValueError:
                                row[i] = None

                        elif header[i] == "timestamp":
                            #timestamp
                            try:
                                row[i] = datetime.datetime.fromisoformat(row[i])
                            except ValueError:
                                row[i] = None

                        else:
                            #float
                            try:
                                row[i] = float(row[i])
                            except ValueError:
                                row[i] = None

                create(sensor_type, row)

                object_count += 1
                print(str(object_count) + ". object created.")

        print("total:", object_count, "objects")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
