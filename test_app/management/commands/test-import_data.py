from django.core.management import BaseCommand
from test_app.models import sps30
import csv

from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import date
from datetime import timedelta
import time
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create

# command example
# python manage.py import_data --url http://archive.sensor.community --date 2023-12-25

class Command(BaseCommand):
    help = 'Load data csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)
        parser.add_argument('--date', type=str)

    def handle(self, *args, **kwargs):

        website = kwargs['url']
        date = kwargs['date']
        base_url = website + "/" + date
        page = requests.get(base_url)
        soup = BeautifulSoup(page.content, "html.parser")

        start = time.time()
        current_sensor_type = None
        for i in soup.find_all("a", href = True):
            if date in i["href"]:
                sensor_type = get_sensor_type(i['href'], date)
                sensor_type = sensor_type.replace("-", "")

                if sensor_type != current_sensor_type:
                    object_count = 0
                    url = base_url + "/" + i["href"]

                    response = urllib.request.urlopen(url)
                    lines = [line.decode("utf-8") for line in response.readlines()]
                    reader = csv.reader(lines, delimiter=";")

                    index = 0
                    for row in reader:
                        # ignore first header row
                        if index == 0:
                            index += 1

                        else:
                            # convert empty string to NaN to avoid type error
                            for i in range(len(row)):
                                if row[i] == "" or row[i] == "unavailable":
                                    row[i] = "nan"

                            if object_count == 0:
                                create(sensor_type, row)

                                object_count += 1
                                print(sensor_type, "successfully created")
                                current_sensor_type = sensor_type

                            else:
                                break

        #print("total:", object_count, "objects")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
