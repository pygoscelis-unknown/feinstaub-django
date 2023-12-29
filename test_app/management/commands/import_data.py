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
# python manage.py import_data-v4 --url http://archive.sensor.community

class Command(BaseCommand):
    help = 'Load data csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)

    def handle(self, *args, **kwargs):

        website = kwargs['url']
        yesterday = date.today() - timedelta(days = 2)
        str_date = str(yesterday)
        base_url = website + "/" + str_date
        page = requests.get(base_url)
        soup = BeautifulSoup(page.content, "html.parser")

        start = time.time()
        object_count = 0
        for i in soup.find_all("a", href = True):
            if str_date in i["href"]:
                sensor_type = get_sensor_type(i['href'], str_date)

                if sensor_type != None:
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

                            create(sensor_type, row)

                            object_count += 1
                            print(str(object_count) + ". object created.")
        print("total:", object_count, "objects")

        end = time.time()
        total_time = end - start
        print("time:", total_time)
