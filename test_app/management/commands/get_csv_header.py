from django.core.management import BaseCommand
import csv
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import date
from datetime import timedelta
import time
from .modules.csv import get_header
from .modules.sensor_type import get_sensor_type
from .modules.sensor_type_queue import register, skip
import json


class Command(BaseCommand):
    help = "get header of csv"

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)
        parser.add_argument('--date', type=str)

    def handle(self, *args, **kwargs):
        website = kwargs['url']
        date = kwargs['date']

        base_url = website + "/" + date + "/"
        page = requests.get(base_url)
        soup = BeautifulSoup(page.content, "html.parser")
        sensor_type_queue = dict()

        for a in soup.find_all("a", href=True):
            sensor_type = get_sensor_type(a["href"], date)

            if sensor_type != None:
                url = base_url + "/" + a["href"]

                if len(sensor_type_queue) == 0:
                    register(sensor_type_queue, sensor_type, url)
                else:
                    if sensor_type not in sensor_type_queue.keys():
                        register(sensor_type_queue, sensor_type, url)
                    else:
                        skip(sensor_type)

        print("writing file ...")
        with open('sensor_csv_header.json', 'w') as file:
            file.write(json.dumps(sensor_type_queue))
        print("see in root path: ./sensor_csv_header.json")
