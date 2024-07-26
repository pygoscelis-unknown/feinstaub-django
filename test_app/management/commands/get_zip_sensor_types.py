from django.core.management import BaseCommand
import csv
import os

from bs4 import BeautifulSoup
import requests
import urllib.request
import zipfile
import datetime
from .modules.sensor_type import get_sensor_type
from .modules.create_object import create

# command example
# python manage.py compare_sensor_types --url http://archive.sensor.community


class Command(BaseCommand):
    help = """
    Print all sensor types saved as csv per month in zip format into json files: see http://archive.sensor.community/csv_per_month/
    """

    def add_arguments(self, parser):
        parser.add_argument("--url", type=str)

    def handle(self, *args, **kwargs):

        url = kwargs["url"] + "/csv_per_month/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        sensor_type_queue = dict()

        filenames = [
            "zip_filenames.json",
            "sensor_types-zip.json",
        ]
        with open(filenames[0], "w") as pyf:
            pyf.write("[\n")
        with open(filenames[1], "w") as pyf:
            pyf.write("[\n")

        sensor_type_queue = []
        index = 0

        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href[-1] == "/":
                href = href[:-1]

            try:
                datetime.datetime.strptime(href, "%Y-%m")
                page = requests.get(url + href + "/")
                soup = BeautifulSoup(page.content, "html.parser")
                date = href

                for a in soup.find_all("a", href=True):
                    if href in a["href"]:
                        sensor_type = get_sensor_type(a["href"], date, True)
                        with open(filenames[0], "a") as pyf:
                            if index == 0:
                                pyf.write('"' + a["href"] + '"')
                            else:
                                pyf.write(',\n"' + a["href"] + '"')

                        if sensor_type not in sensor_type_queue:
                            sensor_type_queue.append(sensor_type)

                            with open(filenames[1], "a") as pyf:
                                if index == 0:
                                    pyf.write('"' + sensor_type + '"')
                                    index += 1
                                else:
                                    pyf.write(',\n"' + sensor_type + '"')
                            print("register sensor type", sensor_type)
                        else:
                            print("sensor type already in queue, skip ...")

            except ValueError:
                continue

        with open(filenames[0], "a") as pyf:
            pyf.write("\n]")
        with open(filenames[1], "a") as pyf:
            pyf.write("\n]")
