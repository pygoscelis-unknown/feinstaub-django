from django.core.management import BaseCommand
import csv

from bs4 import BeautifulSoup
import urllib.request
import zipfile
import datetime
import time
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create

# command example
# python manage.py import_data-zip --url http://archive.sensor.community --year 2024 --month 03 --type bme280

class Command(BaseCommand):
    help = 'Load data from csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)
        parser.add_argument('--year', type=str)
        parser.add_argument('--month', type=str)
        parser.add_argument('--type', type=str)

    def handle(self, *args, **kwargs):

        base_url = kwargs['url']
        year = kwargs['year']
        month = kwargs['month']
        date = year + '-' + month
        sensor_type = kwargs['type']
        url = base_url + "/csv_per_month/" + date + "/" + date + '_' + sensor_type + '.zip'
        file_name = date + "_" + sensor_type

        start = time.time()
        object_count = 0

        print("Downloading zip ...")
        urllib.request.urlretrieve(url, file_name + ".zip")
        with zipfile.ZipFile(file_name + ".zip", 'r') as zip_ref:
            print("Extracting zip ...", end="\r")
            zip_ref.extractall("./")

        with open(file_name + '.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            index = 0
            header = []

            for row in reader:
                # ignore first header row
                if index == 0:
                    for i in range(len(row)):
                        header.append(row[i])
                    index += 1

                else:
                    # convert illegal values
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
                    print(str(object_count) + ". object created.", end="\r")

        print("total:", object_count, "objects", end="\r")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
